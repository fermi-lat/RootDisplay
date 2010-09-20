# -*- python -*-
# $Header: /nfs/slac/g/glast/ground/cvs/RootDisplay/SConscript,v 1.5 2009/11/10 01:29:09 jrb Exp $
# Authors: Heather Kelly <heather@milkyway.gsfc.nasa.gov>
# Version: RootDisplay-00-03-01-gr01
Import('baseEnv')
Import('listFiles')
Import('packages')
progEnv = baseEnv.Clone()
libEnv = baseEnv.Clone()

libEnv.Tool('RootDisplayLib', depsOnly = 1)

RootDisplay = libEnv.SharedLibrary('RootDisplay',
                                   listFiles(['src/*.cxx','src/Dll/*.cxx']))

progEnv.Tool('RootDisplayLib')
progEnv.Tool('GuiSvcLib')
progEnv.Tool('guiLib')

if baseEnv['PLATFORM'] == 'win32':
	progEnv.AppendUnique(LINKFLAGS = ['/include:_GuiSvc_loadRef'])

if baseEnv['PLATFORM'] != 'win32':	
	progEnv.Tool('addLibrary', library = baseEnv['x11Libs'])
# The libraries from the previous statement are located at /usr/X11R6 according to ../gui/cmt/requirements

if baseEnv['PLATFORM'] == 'win32':
	progEnv.Tool('addLibrary', library = ['user32'])
	progEnv.Tool('addLibrary', library = ['gdi32'])
	progEnv.Tool('addLibrary', library = ['winspool'])
	progEnv.Tool('addLibrary', library = ['comdlg32'])
	progEnv.Tool('addLibrary', library = ['shell32'])
	progEnv.Tool('addLibrary', library = ['comdlg32'])
	progEnv.Tool('addLibrary', library = ['shell32'])

#------------

if baseEnv['PLATFORM'] != 'win32':
	progEnv.AppendUnique(LINKFLAGS = ['-u GuiSvc_loadRef'])

#RootDisplayTest = progEnv.Program('RootDisplayTest',listFiles(['src/test/*.cxx']))

progEnv.Tool('registerTargets', package = 'RootDisplay', 
	libraryCxts = [[RootDisplay, libEnv]], 
	includes = listFiles(['RootDisplay/*.h']))




