# $Header: /nfs/slac/g/glast/ground/cvs/GlastRelease-scons/RootDisplay/RootDisplayLib.py,v 1.4 2009/08/27 18:09:21 jrb Exp $
def generate(env, **kw):
    if not kw.get('depsOnly', 0):
        env.Tool('addLibrary', library = ['RootDisplay'])
        if env['PLATFORM']=='win32' and env.get('CONTAINERNAME','')=='GlastRelease':
	    env.Tool('findPkgPath', package = 'RootDisplay') 

    env.Tool('guiLib')
    env.Tool('addLibrary', library = env['gaudiLibs'])
    env.Tool('addLibrary', library = env['rootLibs'])
    if env['PLATFORM']=='win32' and env.get('CONTAINERNAME','')=='GlastRelease':
        env.Tool('findPkgPath', package = 'GuiSvc') 
        env.Tool('findPkgPath', package = 'RootIo') 
	env.Tool('findPkgPath', package = 'rootUtil')
def exists(env):
    return 1;
