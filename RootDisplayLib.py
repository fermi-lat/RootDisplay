# $Header: /nfs/slac/g/glast/ground/cvs/GlastRelease-scons/RootDisplay/RootDisplayLib.py,v 1.3 2009/01/23 00:21:02 ecephas Exp $
def generate(env, **kw):
    if not kw.get('depsOnly', 0):
        env.Tool('addLibrary', library = ['RootDisplay'])
    env.Tool('guiLib')
    env.Tool('addLibrary', library = env['gaudiLibs'])
def exists(env):
    return 1;
