#!~/env/bin/python
# coding: utf-8

# TODO: https://github.com/blueimp/Gallery
# TODO: https://github.com/blueimp/jQuery-File-Upload

from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound
from pyramid.httpexceptions import HTTPException
import os

@view_config(route_name='home', renderer='templates/mytemplate.pt')
def home_view(request):
    return {'project': 'freekrasa'}

@view_config(route_name='root', renderer='templates/root.pt')
def root_view(request):
    mediadir = request.registry.settings["global.mediadir"]
    if os.access(mediadir, os.R_OK):
        root, dirs, files = next(os.walk(mediadir))
        project = "Pójdźże, kiń tę chmurność w głąb flaszy."
        return {'project': project.decode('utf-8'), 'root': root, 'dirs': dirs, 'files': [file.decode('utf-8') for file in files]}
    else:
        raise HTTPNotFound

@view_config(route_name='json', renderer='json')
def json_view(request):
    root, dirs, files = next(walk("/home/dawid/tmp"))
    return {'project': '> freekrasa <', 'root': root, 'dirs': dirs, 'files': files}

@view_config(route_name='string', renderer='string')
def json_view(request):
    root, dirs, files = next(walk("/home/dawid/tmp"))
    return {'project': '> freekrasa <'}

@view_config(context=HTTPException, renderer='templates/exception.pt')
def not_found_view(ex, request):
    return {'ex': ex}
