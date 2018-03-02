'use strict'

import Viewer from './components/Viewer.vue'
import TaxonomyItem from './components/TaxonomyItem.vue'
import NewFileForm from './components/Forms/NewFileForm.vue'

// Custom resource types.
tozti.addResourceType(
    'media/file',
    'upload', 'fichier', 'm',
    TaxonomyItem,
    Viewer,
    NewFileForm
)