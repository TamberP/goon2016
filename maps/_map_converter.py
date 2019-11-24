# By qwertyqwerty to help ease ZeWaka's pain
import re
import sys
import codecs
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = ' '):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
    # Print New Line on Complete
    if iteration == total:
        print()

icon_state_map = {"floor": "Vspace/brig", "floorscorched1": "scorched", "floorscorched2": "scorched2", "damaged1": "damaged1", "damaged2": "damaged2", "damaged3": "damaged3", "damaged4": "damaged4", "damaged5": "damaged5", "plating": "plating", "panelscorched": "plating/scorched", "platingdmg1": "plating/damaged1", "platingdmg2": "plating/damaged2", "platingdmg3": "plating/damaged3", "floorgrime": "grime", "fullneutral": "neutral", "neutral": "neutral/side", "neutralcorner": "neutral/corner", "white": "white", "whitehall": "white/side", "whitecorner": "white/corner", "whitecheck": "white/checker", "whitecheck2": "white/checker2", "floorgrime-w": "white/grime", "dark": "black", "greyblack": "black/side", "greyblackcorner": "black/corner", "floorgrime-b": "black/grime", "darkwhite": "blackwhite", "darkwhitecorner": "blackwhite/corner", "whiteblack": "blackwhite/side", "floorgrime_bw1": "blackwhite/whitegrime", "floorgrime_bw2": "blackwhite/whitegrime/other", "fullblack": "grey", "black": "grey/side", "blackcorner": "grey/corner", "blackchecker": "grey/checker", "floorgrime_gb1": "grey/blackgrime", "floorgrime_gb2": "grey/blackgrime/other", "floorgrime_gw1": "grey/whitegrime", "floorgrime_gw2": "grey/whitegrime/other", "fullred": "red", "red": "red/side", "redcorner": "red/corner", "redchecker": "red/checker", "redblack": "redblack", "redblackcorner": "redblack/corner", "redwhite": "redwhite", "redwhitecorner": "redwhite/corner", "fullblue": "blue", "blue": "blue/side", "bluecorner": "blue/corner", "bluechecker": "blue/checker", "blueblack": "blueblack", "blueblackcorner": "blueblack/corner", "bluewhite": "bluewhite", "bluewhitecorner": "bluewhite/corner", "fulldblue": "darkblue", "blue-dblue": "darkblue/checker", "blue-dblue2": "darkblue/checker/other", "blugreenfull": "bluegreen", "blugreen": "bluegreen/side", "blugreencorner": "bluegreen/corner", "fullgreen": "green", "green": "green/side", "greencorner": "green/corner", "greenchecker": "green/checker", "greenblack": "greenblack", "greenblackcorner": "greenblack/corner", "greenwhite": "greenwhite", "greenwhitecorner": "greenwhite/corner", "toxshuttle": "greenwhite/other", "toxshuttlecorner": "greenwhite/other/corner", "fullpurple": "purple", "purple": "purple/side", "purplecorner": "purple/corner", "purplechecker": "purple/checker", "purpleblack": "purpleblack", "purpleblackcorner": "purpleblack/corner", "purplewhite": "purplewhite", "purplewhitecorner": "purplewhite/corner", "fullyellow": "yellow", "yellow": "yellow/side", "yellowcorner": "yellow/corner", "yellowchecker": "yellow/checker", "yellowblack": "yellowblack", "yellowblackcorner": "yellowblack/corner", "fullorange": "orange", "orange": "orange/side", "orangecorner": "orange/corner", "fullcaution": "orangeblack", "caution": "orangeblack/side", "cautionwhite": "orangeblack/side/white", "cautioncorner": "orangeblack/corner", "cautionwhitecorner": "orangeblack/corner/white", "circuit": "circuit", "circuit-green": "circuit/green", "circuit-white": "circuit/white", "circuit-purple": "circuit/purple", "circuit-red": "circuit/red", "circuit-vint1": "circuit/vintage", "circuitoff": "circuit/off", "red1": "carpet", "grimy": "carpet/grime", "arcade_carpet": "carpet/arcade", "arcade_carpet_half": "carpet/arcade/half", "arcade_carpet_blank": "carpet/arcade/blank", "office_carpet": "carpet/office", "office_carpet2": "carpet/office/other", "shiny": "shiny", "whiteshiny": "shiny/white", "arcade": "specialroom/arcade", "bar": "specialroom/bar", "bar-edge": "specialroom/bar/edge", "boxing": "specialroom/gym", "gym_mat": "specialroom/gym/alt", "cafeteria": "specialroom/cafeteria", "chapel": "specialroom/chapel", "freezerfloor": "specialroom/freezer", "freezerfloor2": "specialroom/freezer/white", "freezerfloor3": "specialroom/freezer/blue", "medbay": "specialroom/medbay", "arrival": "arrival", "arrivalcorner": "arrival/corner", "escape": "escape", "escapecorner": "escape/corner", "delivery": "delivery", "delivery_white": "delivery/white", "deliverycaution": "delivery/caution", "bot": "bot", "bot_white": "bot/white", "bot_blue": "bot/blue", "botcaution": "bot/caution", "engine": "engine", "engine-glow": "engine/glow", "engine-blue": "engine/glow/blue", "engine_caution_south": "engine/caution/south", "engine_caution_north": "engine/caution/north", "engine_caution_ns": "engine/caution/northsouth", "engine_caution_west": "engine/caution/west", "engine_caution_east": "engine/caution/east", "engine_caution_we": "engine/caution/westeast", "engine_caution_corners": "engine/caution/corner", "engine_caution_corners2": "engine/caution/corner2", "engine_caution_misc": "engine/caution/misc", "caution_south": "caution/south", "caution_north": "caution/north", "caution_ns": "caution/northsouth", "caution_west": "caution/west", "caution_east": "caution/east", "caution_we": "caution/westeast", "corner_east": "caution/corner/se", "corner_west": "caution/corner/sw", "corner_neast": "caution/corner/ne", "corner_nwest": "caution/corner/nw", "floor_hazard_corners": "caution/corner/misc", "floor_hazard_misc": "caution/misc", "wooden-2": "wood", "wooden": "wood/two", "wooden-3": "wood/three", "wooden-4": "wood/four", "Stairs_alone": "stairs", "Stairs_wide": "stairs/wide", "Stairs2_wide": "stairs/wide/other", "Stairs_wide_green": "stairs/wide/green", "stairs_middle": "stairs/wide/middle", "medstairs_alone": "stairs/medical", "medstairs_wide": "stairs/medical/wide", "medstairs2_wide": "stairs/medical/wide/other", "medstairs_middle": "stairs/medical/wide/middle", "quiltystair": "stairs/quilty", "quiltystair2": "stairs/quilty/wide", "wood_stairs": "stairs/wood", "wood_stairs2": "stairs/wood/wide", "wood2_stairs": "stairs/wood2", "wood2_stairs2": "stairs/wood2/wide", "wood3_stairs": "stairs/wood3", "wood3_stairs2": "stairs/wood3/wide", "dark_stairs": "stairs/dark", "dark_stairs2": "stairs/dark/wide", "flashyblue": "Vspace", "vrfloor": "Vspace/brig", "vrplating": "Vspace/brig", "vrspace": "Vspace/brig", "vrwhitehall": "Vspace/brig", "snow1": "snow", "snowgreen": "snow/green", "snowgreencorner": "snow/green/corner", "sand": "sand", "grass": "grass", "grass_eh": "grass/random/alt", "metalfoam": "metalfoam", "bridge": "blob", "ironform": "metalfoam"}

if len(sys.argv)>=2:
    try:
        mapstr = codecs.open(sys.argv[1], 'r', 'latin-1').read()
        print("Loaded {}".format(sys.argv[1]))
    except:
        print("Cannot find file: {}".format(sys.argv[1]))
        exit()
else:
    print("Usage: map_converter.py <input map file> [output map file]")
    exit()

i=1
for state,path in icon_state_map.items():
    find = r'\/turf\/(un)*simulated\/floor(?:\/plating)*(\/airless)*{(?:dir = (\d{1,10})+)*[^\n]*(?:icon_state = "[ICONSTATE]")+(?:; dir = (\d{1,10})+)*[\W\w]*?}'.replace("[ICONSTATE]", state)
    sub = r'/turf/\g<1>simulated/floor\g<2>/[PATH]{dir = \g<3>\g<4>}'.replace("[PATH]", path)
    mapstr = re.sub(find, sub, mapstr)
    printProgressBar(i, len(icon_state_map.keys()), prefix = 'Converting:', length = 50)
    i+= 1

output_filename = sys.argv[2] if len(sys.argv) >= 3 else "output.dmm"

mapstr = mapstr.replace("/turf/simulated/floor/grid", "/turf/simulated/floor/circuit")
mapstr = mapstr.replace("/turf/simulated/floor/plating/airless/catwalk", "/turf/simulated/floor/airless/plating/catwalk")
mapstr = mapstr.replace("/turf/unsimulated/floor/grid", "/turf/unsimulated/floor/circuit")
mapstr = mapstr.replace("/turf/unsimulated/floor/plating/airless/catwalk", "/turf/unsimulated/floor/airless/plating/catwalk")
mapstr = mapstr.replace("{dir = }", "")

f = codecs.open(output_filename, "w", "latin-1")
f.write(mapstr)
f.close()

print("Saved as {}".format(output_filename))
