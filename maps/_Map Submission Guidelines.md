# Goonstation Map Submission Guidelines

## Required

###### These are fundamental map features that need to be checked to be working prior to submission.

If these features do not work in the **2016 release** then your map will be **rejected** and ineligible for resubmission for a full calendar month. If these features are found to not work in the latest codebase, but do work in the 2016 release, you are off the hook.

- Crates should be able to be ordered from cargo, and arrive where expected **without player intervention**. Sitting in a few-tile conveyor "airlock"  is fine (see Destiny), sitting outside because the door did not open at all is not; missing the conveyor entirely is definitely not fine.

- Crates should be able to be sold from cargo from the expected conveyor belt **without player intervention**. Having to open a few-tile conveyor "airlock" is fine (see Destiny).

- **Access levels** (for both doors and machinery, e.g. NanoMeds, AI turrets) should be correct. Missing a small handful is acceptable, but if excess access levels are incorrect (at the coders' discretion) the map will be rejected. Using the new access_spawn objects is required.

- Wiring and pipes (disposals, mail, brig, and morgue/crematorium, if present) should be **complete and error-free** for the most part. Obviously, it is okay if you are missing a single wire or something.

- Note to above: SpyGuy and Haine made a wonderful tool to test disposal networks, it is included in the maps/ folder.

- The disposals crusher blast door should be **closed** at round start (i.e. anything put down disposals at round start should not be crushed without someone opening the door).

- **All areas** on station should be powered. APCs should be able to be charging if the appropriate SMES are set to output.

- Networked equipment should be **functional**. Specifically: telescience teleporter, communications consoles/dishes.

- A tested and **functioning engine**, either thermo-electric or singularity. Please provide a screenshot of the engine output if thermo-electric (not necessarily at hellburn levels, but enough to meet the station/ship's power needs)

- A **tested and functioning** toxins, if there is a toxins on the map.

- **Working** shuttles, for the escape shuttle, mining and visiting traders. Some maps can have different facing traders which are not present in the release. If so, please let the coders know when you are submitting your map.

- **Correctly placed spawn points** for all present jobs, late-joiners, observers and so on. Failing to place these will result in players being dropped in to 1,1, which is a Bad Thing.

- A **correctly linked** up syndicate listening post (i.e. nuclear operatives should be able to teleport there), and the airlocks should absolutely be correctly configured.

- A **Correctly placed** landmark for the Map at 1,1.

- **Windows** should be placed using the `obj/wingrille_spawn` spawners.

- **Drains**, the path is `/obj/machinery/drainage`. It won't actually drain anything, but it'll convert into one that does.

## Recommended
###### These are generally recommended map features that should probably be present in your map. If they are present, please ensure they work as intended.
- An owlery or aviary.
- Monkeys spawn landmarks (including a place for Stirstir in the brig)
- Functioning buddy-paths. Including a tour guide written for Murray/Tour Buddy.
- If you are using perspective walls, try to minimize placing objects on the south side of rooms.
- Blobstart, peststart, and halloweenspawn landmarks.
- Medbay and Security should be well-thought out, daresay more so than other departments.
- Arrivals should have more than one exit, to prevent people from being unable to join the game.
- Cloning should follow the style of modern maps and be mostly public access.
- Feel free to take inspiration from other maps, but please don't copy paste large parts of them.

####  Turf Replacements

## Addendum: Thanks to a tool coded by qwertyqwerty, all the maps have been updated to use modern paths. So, you don't really need to use the below methods anymore, but it's there for posterity.

Goonstation now primarily uses pathed floors instead of instanced versions of `/turf/simulated/floor`. For example, `/turf/simulated/floor/red/corner` is a tile that is grey with red corners in the cardinal directions for its direction states. Because of this change, maps should be primarily made from scratch and not from copied parts of old maps. It is possible to convert old maps,

- All of `/turf/simulated/floor/grid` must be changed to `/turf/simulated/floor/circuit`

- All of `/turf/simulated/floor/plating/airless/catwalk` must be changed to `/turf/simulated/floor/airless/plating/catwalk`

- All maps must **not use** instanced floors for the majority of their turfs.

##### To convert existing maps to non-instanced format follow this simple guide.

**(RECOMMENDED)** Get a editor other than Dream Maker.

1. Open the advanced Find/Replace fuctionality.
2. Use this non-confusing RegEx in the 'Find' section: `\/turf\/(un)*simulated\/floor(?:\/plating)*(\/airless)*{(?:dir = (\d{1,10})+)*[^\n]*(?:icon_state = "yellow")+(?:; dir = (\d{1,10})+)*[\W\w]*?}`
3. Make sure you're only modifying files in the maps folder.
4. Set the replacement to be this RegEx: `/turf/$1simulated/floor$2/yellow/side{dir = $3$4}`

Now, what's currently inputted into the RegEx is an example.
What it currently does is change a tile with the "yellow" icon_state into a floor of yellow/side

To change something other than a tile with the "yellow" icon_state, put that icon state in the find.
You'll also need to change the replacement to be the tile that you want.

For example, if I wanted to change the a tile with the icon_state arcade_carpet" into /turf/simulated/floor/carpet/arcade, I would use this for my find RegEx:
`\/turf\/(un)*simulated\/floor(?:\/plating)*(\/airless)*{(?:dir = (\d{1,10})+)*[^\n]*(?:icon_state = "arcade_carpet")+(?:; dir = (\d{1,10})+)*[\W\w]*?}`
Also, I would need to put this in my replace box:
`/turf/$1simulated/floor$2/carpet/arcade{dir = $3$4}`

This RegEx must be done for every floor path/icon_state in floors.dm if you want to convert a map.

That's all to it! If you have any questions about this RegEx replace for converting maps, visit #imcoder on SynIRC or the Goonstation Discord.
