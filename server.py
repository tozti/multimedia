"""
A tozti extension providing file uploads.
"""
__license__ = 'AGPL'
__author__ = 'The tozti Project'
__email__ = 'tozti@ens-lyon.fr'


"""The schema for a file."""
FILE_SCHEMA = {
    'body': {
        'name': {
            'type': 'string'
        },
        'handle': {
            'type': 'string'
        },
        'filename': {
            'type': 'string'
        },
        'file': {
            'type': 'upload',
            'acceptable': ['image/jpg']
        }
    }
}


MANIFEST = {
    'name': 'media',
    'includes': ['build.js', 'css/style.css'],
    'types': {
        'file': FILE_SCHEMA
    },
}
