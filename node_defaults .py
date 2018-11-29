##################NODE DEFAULTS##################
#ROTONODE
nuke.knobDefault('Roto.output','alpha')

#EXPTOOL
nuke.knobDefault('EXPTool.mode','Stops')
nuke.knobDefault('EXPTool.label','[value mode]')
#BlurNode
nuke.knobDefault('Blur.channels','rgba')
#Defocus
nuke.knobDefault('Defocus.channels','rgba')
#median
nuke.knobDefault('Median.size','2')
#Dilate
nuke.knobDefault('Dilate.channels','rgba')
#VectorBlur
nuke.knobDefault('VectorBlur.channels','rgba')
#Sharpen
nuke.knobDefault('Sharpen.channels','rgba')
#curvetool
nuke.knobDefault('CurveTool.avgframes','1')
#read
nuke.knobDefault('Read.after','hold')
#read
nuke.knobDefault('Read.before','hold')
#shutteroffset
nuke.knobDefault('shutteroffset','center')
#shuffle
nuke.knobDefault('Shuffle.label','[value in]')
#TextNode Frame padding to 4
nuke.knobDefault('Text.message',' frame [format %04d [frame]] ')
#PostageStamp Label
nuke.knobDefault('PostageStamp.label','[lindex [split [basename [value [topnode].file]] .] 0]')
#read_local cache File ALWAYS
nuke.knobDefault('Read.cacheLocal','always')

