#Thank you for using this
#
#   1. Install the Add-on
#   2. set up the hotkey
#
#       For getting this to work, a hotkey has to be set up.
#       Under "Keymap", go to "3D View", "3D View (Global)", scroll down and add a new Operator
#       change the value of the none to "call_menu_pie"
#       and the name to "mesh.viewpie"
#
#   hf using <3





import bpy
from bpy.types import Menu, Operator

bl_info = {
        "name": "View Axis Pie Menu",
        "author": "Jan Wiesemann",
        "version": (4, 2, 0, 0),
        "description": "Pie Menu for Front-, Side-, Topview etc.",
        "blender": (2, 80, 0),
        "category": "3D view"
}



class VIEW3D_MT_PIE_template(Menu):
    # label is displayed at the center of the pie menu.
    bl_label = "Operation"
    bl_idname="mesh.viewpie"
    
    def draw(self, context):
        
        layout = self.layout
        
        pie = layout.menu_pie()
        pie.operator("3d.view")
        
        
        
def register():
    bpy.utils.register_class(VIEW3D_MT_PIE_template)
    bpy.utils.register_class(View)
    
    
def unregister():
    bpy.utils.unregister_class(VIEW3D_MT_PIE_template)
    bpy.utils.unregister_class(View)
    
    
if __name__ == "__main__":
    register()
    
    bpy.ops.wm.call_menu_pie(name="VIEW3D_MT_PIE_template")
    
    
class View(Operator):
    bl_idname = "3d.view"
    bl_label = "3DView"
    
    def execute(self, context):
        bpy.ops.view3d.view_axis
        
        return {'FINISHED'}
