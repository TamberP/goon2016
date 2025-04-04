/datum/puzzlewizard/button
	name = "AB CREATE: Button (single state)"
	var/color_rgb = ""
	var/button_type
	var/button_name
	var/button_density = ""
	var/list/selected_triggerable = list()
	var/selection

	initialize()
		selection = unpool(/obj/adventurepuzzle/marker)
		button_type = input("Button type", "Button type", "ancient") in list("ancient", "red", "runes")
		color_rgb = input("Color", "Color", "#ffffff") as color
		button_name = input("Button name", "Button name", "button") as text
		var/bdstr = input("Is the button dense (impassable)?", "Passability", "yes") in list("yes", "no")
		button_density = (bdstr == "yes") ? 1 : 0
		boutput(usr, "<span style=\"color:blue\">Left click to place buttons, right click triggerables to (de)select them for automatic assignment to the buttons. Ctrl+click anywhere to finish.</span>")
		boutput(usr, "<span style=\"color:blue\">NOTE: Select stuff first, then make buttons for extra comfort!</span>")

	proc/clear_selections()
		for (var/obj/O in selected_triggerable)
			O.overlays -= selection
		selected_triggerable.len = 0

	disposing()
		clear_selections()
		pool(selection)

	build_click(var/mob/user, var/datum/buildmode_holder/holder, var/list/pa, var/atom/object)
		if (pa.Find("left"))
			var/turf/T = get_turf(object)
			if (pa.Find("ctrl"))
				finished = 1
				clear_selections()
				return
			if (T)
				var/obj/adventurepuzzle/triggerer/button/button = new /obj/adventurepuzzle/triggerer/button(T)
				button.name = button_name
				button.dir = holder.dir
				button.icon_state = "button_[button_type]_unpressed"
				button.button_type = button_type
				button.density = button_density
				button.triggered = selected_triggerable.Copy()
				spawn(10)
					button.color = color_rgb
		else if (pa.Find("right"))
			if (istype(object, /obj/adventurepuzzle/triggerable))
				if (object in selected_triggerable)
					object.overlays -= selection
					selected_triggerable -= object
				else
					var/list/actions = object:trigger_actions()
					if (islist(actions) && actions.len)
						var/act_name = input("Do what?", "Do what?", actions[1]) in actions
						var/act = actions[act_name]
						object.overlays += selection
						selected_triggerable += object
						selected_triggerable[object] = act
					else
						boutput(usr, "<span style=\"color:red\">ERROR: Missing actions definition for triggerable [object].</span>")

/obj/adventurepuzzle/triggerer/button
	icon = 'icons/obj/randompuzzles.dmi'
	name = "button"
	desc = "A button. Perhaps it opens something? Or something worse?"
	icon_state = "button_red_unpressed"
	density = 0
	opacity = 0
	anchored = 1
	var/button_type = "red"
	var/pressed = 0

	attack_hand(var/mob/living/user as mob)
		if (!istype(user))
			return
		if (!(user in range(1)))
			boutput(user, "<span style=\"color:red\">You must go closer!</span>")
			return
		if (!pressed)
			pressed = 1
			icon_state = "button_[button_type]_pressed"
			post_trigger()
			spawn(20)
				icon_state = "button_[button_type]_unpressed"
				pressed = 0

	serialize(var/savefile/F, var/path, var/datum/sandbox/sandbox)
		..()
		F["[path].button_type"] << button_type

	deserialize(var/savefile/F, var/path, var/datum/sandbox/sandbox)
		. = ..()
		F["[path].button_type"] >> button_type

/obj/adventurepuzzle/triggerer/bookcase
	name = "bookcase"
	desc = "A wooden furniture used for the storage of books. One of the books appears to be loose."
	density = 0
	opacity = 0
	anchored = 1
	icon = 'icons/turf/adventure.dmi'
	icon_state = "bookcase_full_alone_button"
	var/pressed = 0
	var/obj/overlay/tile_effect/secondary/effect_overlay

	disposing()
		if (effect_overlay)
			effect_overlay.loc = null
			qdel(effect_overlay)
			effect_overlay = null
		..()

	Del()
		if (effect_overlay)
			qdel(effect_overlay)
		..()

	New(var/L)
		..()
		src.effect_overlay = new/obj/overlay/tile_effect/secondary/bookcase(loc)
		set_dir(dir)
		// if (isturf(loc))
		// 	if (loc:effect_overlay)
		// 		effect_overlay.color = loc:effect_overlay.color

	onVarChanged(var/varname, var/oldvalue, var/newvalue)
		if (varname == "dir")
			set_dir(newvalue)

	proc/set_dir(var/D)
		dir = D
		if (!(dir & 2))
			dir = 2
		pixel_y = 28
		effect_overlay.dir = dir

	attack_hand(var/mob/user)
		if (user.y != src.y || user.x < src.x - 1 || user.x > src.x + 1)
			return 0
		if (!pressed)
			pressed = 1
			icon_state = "bookcase_full_alone_0"
			post_trigger()
