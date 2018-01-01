from tozti.utils import RouterDef
from aiohttp import web


router = RouterDef()

MANIFEST = {
    'router': router,
    'includes': ['build.js'],
}
