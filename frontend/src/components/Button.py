import flet as ft


class Button(ft.CupertinoButton):
    
    def __init__(self, page: ft.Page,text = None, icon = None, icon_color = None, content = None, bgcolor = None, color = None, disabled_bgcolor = None, opacity_on_click = None, min_size = None, padding = None, alignment = None, border_radius = None, url = None, url_target = None, on_click = None, on_long_press = None, on_focus = None, on_blur = None, ref = None, key = None, width = None, height = None, left = None, top = None, right = None, bottom = None, expand = None, expand_loose = None, col = None, opacity = None, rotate = None, scale = None, offset = None, aspect_ratio = None, animate_opacity = None, animate_size = None, animate_position = None, animate_rotation = None, animate_scale = None, animate_offset = None, on_animation_end = None, tooltip = None, badge = None, visible = None, disabled = None, data = None):
        super().__init__(text, icon, icon_color, content, bgcolor, color, disabled_bgcolor, opacity_on_click, min_size, padding, alignment, border_radius, url, url_target, on_click, on_long_press, on_focus, on_blur, ref, key, width, height, left, top, right, bottom, expand, expand_loose, col, opacity, rotate, scale, offset, aspect_ratio, animate_opacity, animate_size, animate_position, animate_rotation, animate_scale, animate_offset, on_animation_end, tooltip, badge, visible, disabled, data)
        
        self.page = page
        
        self.width = self.page.width
        self.height = 50
        
        self.border_radius = 10
        
        self.text = text
