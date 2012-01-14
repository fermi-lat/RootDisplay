# -*- python -*-
# $Header: /nfs/slac/g/glast/ground/cvs/RootDisplay/SConscript,v 1.9 2012/01/14 22:10:14 jrb Exp $
# Authors: Heather Kelly <heather@milkyway.gsfc.nasa.gov>
# Version: RootDisplay-00-04-01
Import('baseEnv')
Import('listFiles')
Import('packages')
progEnv = baseEnv.Clone()
libEnv = baseEnv.Clone()

libEnv.Tool('addLinkDeps', package='RootDisplay', toBuild='component')

RootDisplay =libEnv.ComponentLibrary('RootDisplay',
				     listFiles(['src/*.cxx']))

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


#RootDisplayTest = progEnv.GaudiProgram('RootDisplayTest',listFiles(['src/test/*.cxx']), test=0, package='RootDisplay')

progEnv.Tool('registerTargets', package = 'RootDisplay', 
	     libraryCxts = [[RootDisplay, libEnv]], 
	     includes = listFiles(['RootDisplay/*.h']),
	     jo = ['src/defaultRootDisplayOptions.txt',
		   'src/test/jobOptions.txt'])




