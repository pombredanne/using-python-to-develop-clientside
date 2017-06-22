from url import fmap

Vue = require('vue')
VueRouter = require('vue-router')
Vue.use(VueRouter)

window.noop = lambda: False

ace = []
for p, h in fmap.items():
    ace.append({
        'path': p,
        'component': h,
    })
    pass

def init():
    router = __new__(VueRouter({
        'mode': 'history',
        'routes': ace,
    }))

    window.app = app = __new__(Vue({
        'router': router,
    }))

    app['$mount']('#app')
    pass

init()
