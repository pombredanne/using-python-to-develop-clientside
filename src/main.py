import common
from url import fmap

Vue = require('vue')
VueRouter = require('vue-router')
VueMaterial = require('vue-material')
Vuex = require('vuex')
Vue.use(VueRouter)
Vue.use(VueMaterial)
Vue.use(Vuex)

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
