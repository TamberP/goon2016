// How 2 use: run /proc/test_disposal_system via Advanced ProcCall
// locate the X and Y where normally disposed stuff should end up (usually the last bit of conveyor belt in front of the crusher door
// wait and see what comes up!
/proc/test_disposal_system(var/expected_x, var/expected_y, var/sleep_time = 600, var/test_path = "/obj/machinery/disposal")
	if (!usr && (isnull(expected_x) || isnull(expected_y)))
		return
	if (isnull(expected_x))
		expected_x = input(usr,"Please enter X coordinate") as null|num
		if (isnull(expected_x))
			return
	if (isnull(expected_y))
		expected_y = input(usr,"Please enter Y coordinate") as null|num
		if (isnull(expected_y))
			return

	var/list/dummy_list = list()
	for (var/obj/machinery/disposal/D in world)
		if (D.z != 1)
			break
		/*
		if (D.type != text2path(test_path))
			continue
		*/
		var/obj/item/disposal_test_dummy/TD
		// Mail chute test
		if(istype(D, /obj/machinery/disposal/mail))
			var/obj/machinery/disposal/mail/mail_chute = D

			mail_chute.Topic("?rescan=1", params2list("rescan=1"))
			spawn(20)
				for(var/dest in mail_chute.destinations)
					var/obj/item/disposal_test_dummy/mail_test/MD = new /obj/item/disposal_test_dummy/mail_test(mail_chute)
					MD.source_disposal = mail_chute
					MD.destination_tag = dest
					mail_chute.destination_tag = dest
					//dummy_list.Add(MD)
					mail_chute.flush()

		else
			//Regular chute
			TD = new /obj/item/disposal_test_dummy(D)
			TD.expected_x = expected_x
			TD.expected_y = expected_y
			dummy_list.Add(TD)
			TD.source_disposal = D
			spawn(0)
				D.flush()

	message_coders("test_disposal_system() sleeping [sleep_time] and spawned [dummy_list.len] dummies")
	sleep(sleep_time)

	var/successes = 0
	for (var/obj/item/disposal_test_dummy/TD in dummy_list)
		if (!TD.report_fail())
			successes ++
		
		qdel(TD)

	message_coders("Disposal test completed with [successes] successes")

/obj/item/disposal_test_dummy
	icon = 'icons/misc/bird.dmi'
	icon_state = "bhooty"
	name = "wtf"
	var/obj/machinery/disposal/source_disposal = null
	var/expected_x = 0
	var/expected_y = 0

	proc/report_fail()
		if(src.x != expected_x || src.y != expected_y)
			message_coders("test dummy misrouted at [log_loc(src)][src.source_disposal ? " from [log_loc(src.source_disposal)]" : " (source disposal destroyed)"]")
			return 1

		return 0

/obj/item/disposal_test_dummy/mail_test
	var/obj/machinery/disposal/mail/destination_disposal = null
	var/destination_tag = null
	var/success = 0

/obj/item/disposal_test_dummy/mail_test/pipe_eject()
	destination_disposal = locate(/obj/machinery/disposal/mail) in src.loc
	if(destination_disposal && destination_disposal.mail_tag == destination_tag)
		success = 1
	spawn(50)
		report_fail()
		qdel(src)
	..()

/obj/item/disposal_test_dummy/mail_test/report_fail()
	if(!success)
		message_coders("mail dummy misrouted at [log_loc(src)] from [log_loc(source_disposal)], destination: [destination_tag], reached: [log_loc(destination_disposal)]")
		return 1
	return 0