# -*- python -*-
# $Header: /nfs/slac/g/glast/ground/cvs/RootDisplay/SConscript,v 1.11 2012/01/20 22:50:41 jrb Exp $
# Authors: Heather Kelly <heather@milkyway.gsfc.nasa.gov>
# Version: RootDisplay-00-04-02
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

if baseEnv['PLATFORM'] == 'win32':
	progEnv.Tool('addLibrary', library = ['user32'])
	progEnv.Tool('addLibrary', library = ['gdi32'])
	progEnv.Tool('addLibrary', library = ['winspool'])
	progEnv.Tool('addLibrary', library = ['comdlg32'])
	progEnv.Tool('addLibrary', library = ['shell32'])
	progEnv.Tool('addLibrary', library = ['comdlg32'])
	progEnv.Tool('addLibrary', library = ['shell32'])


#RootDisplayTest = progEnv.GaudiProgram('RootDisplayTest',listFiles(['src/test/*.cxx']), test=0, package='RootDisplay')

progEnv.Tool('registerTargets', package = 'RootDisplay', 
	     libraryCxts = [[RootDisplay, libEnv]], 
	     includes = listFiles(['RootDisplay/*.h']),
	     jo = ['src/defaultRootDisplayOptions.txt',
		   'src/test/jobOptions.txt'])




