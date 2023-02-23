#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import annotations
import matplotlib.pylab as plt


class Arc:
    uid = 0
    
    def __int__(self,
                uid: str = '',
                radius: float = 1000,
                width: float = 1,
                bottom: float = 500,
                top: float = 550,
                face_color: str = '',
                edge_color: str = '#303030',
                line_width: float = 1.0,
                label: str = '',
                label_position: float = 0,
                label_size: float = 10,
                label_visible: bool = False):
        
        self.uid = uid if uid else Arc.uid
        assert isinstance(self.uid, str), TypeError(f'Invalid uid {uid}, uid must provide as a string.')

        self.radius = radius
        assert isinstance(radius, float), TypeError(f'Invalid radius {radius}, radius must provide as a number')

        self.width = width
        assert isinstance(width, float), TypeError(f'Invalid width {width}, width must provide as a number')
        
        self.bottom = bottom
        assert isinstance(bottom, float), TypeError(f'Invalid bottom {bottom}, bottom must provide as a number')

        self.top = top
        assert isinstance(top, float), TypeError(f'Invalid top {top}, top must provide as a number')
        
        self.face_color = face_color
        self.edge_color = edge_color
        self.line_width = width
        self.label = label if label else self.uid
        self.label_position = label_position
        self.label_size = label_size
        self.label_visible = label_visible
        
        Arc.uid += 1
        

class Circle:
    """
    A Circle object provides a circle whose radius is 1000 (a.u.) as a drawing space.
    Any graph (line, scatter, bar, heatmap, and chord) can be placed on the space by
    specifying the bottom (0 - 1000) and top (0 - 1000) and the corresponding Arc object.
    """
    
    def __init__(self,
                 fig: plt.figure | None = None,
                 fig_size: list | tuple | None = None,
                 start: float = 0,
                 end: float = 360):
        self.fig_size = fig_size if fig_size else (6, 6)
        self.fig = plt.figure(figsize=fig_size) if fig is None else fig
        self.arcs = {}
        
    def add_arc(self, arc):
        self.arcs[arc.uid] = arc
        

if __name__ == '__main__':
    pass
