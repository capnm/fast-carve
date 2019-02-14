import bpy
from bpy.types import Operator
from bpy.props import StringProperty

# Set the pivot point of the active object
# to the center and add a mirror modifier
class FC_MirrorOperator(Operator):
    bl_idname = "object.mirror"
    bl_label = "Center Origin & Mirror"
    bl_description = "Mirror selected object" 
    bl_options = {'REGISTER', 'UNDO'} 
    
    @classmethod
    def poll(cls, context):
        
        mode = context.active_object.mode       
        return len(context.selected_objects) == 1 and mode == "OBJECT"
    
    def execute(self, context):
        
        cursor_location = bpy.context.scene.cursor_location.copy()
                
        bpy.context.scene.cursor_location = (0.0, 0.0, 0.0)
        
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
        
        bpy.ops.object.modifier_add(type='MIRROR')    
        
        bpy.context.scene.cursor_location = cursor_location

        return {'FINISHED'}

#3D cursor center
class FC_3DCursorOperator(Operator):
    bl_idname = "view3d.cursor_center"
    bl_label = "Center cursor"
    bl_description = "Set the 3D cursor to center" 
    bl_options = {'REGISTER', 'UNDO'} 

    def execute(self, context):       
        bpy.ops.view3d.snap_cursor_to_center()
        return {'FINISHED'}  

# Dissolve
class FC_DissolveEdgesOperator(Operator):
    bl_idname = "view3d.dissolve_edges"
    bl_label = "Dissolve edges"
    bl_description = "Dissolve the selected edges" 
    bl_options = {'REGISTER', 'UNDO'} 

    @classmethod
    def poll(cls, context):
        
        mode = context.active_object.mode       
        return len(context.selected_objects) == 1 and mode == "EDIT"

    def execute(self, context):       
        bpy.ops.mesh.dissolve_edges()
        return {'FINISHED'}  


# Symmetrize  
class FC_SymmetrizeOperator(Operator):
    bl_idname = "object.sym"
    bl_label = "Symmetrize"
    bl_description = "Symmetrize selected object" 
    bl_options = {'REGISTER', 'UNDO'}
    
    sym_axis = StringProperty(name="Symmetry axis", options={'HIDDEN'}, default="NEGATIVE_X")
    
        
    @classmethod
    def poll(cls, context):
        
        mode = context.active_object.mode       
        return len(context.selected_objects) == 1 and mode == "OBJECT"
    

    def execute(self, context):
        
        bpy.ops.object.mode_set(mode="EDIT")
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.symmetrize(direction=self.sym_axis)
        bpy.ops.object.mode_set(mode="OBJECT")
        
        return {'FINISHED'}