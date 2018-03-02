<template>
    <t-new-resource-form
        title="Envoyer un fichier"
        :resource="file"
        :callback="attemptNewFile"
        :parent="$parent"
        :root="root">
        <b-field label-for="file" label="Fichier">
            <b-input
                type="file"
                ref="file"
                required>
            </b-input>
        </b-field>
    </t-new-resource-form>
</template>

<script>
    export default {
        props: {
            root: {
                type: Object,
                default: null,
                validate(root) {
                    return root && [
                        'core/group',
                        'core/folder',
                    ].indexOf(root.type) > -1
                }
            }
        },

        data() {
            return {
                file: {
                    name: '',
                    handle: '',
                },
            }
        },

        methods: {
            attemptNewFile(handler) {
                // let prom = tozti
                //     // Create the thread.
                //     .store.create({
                //         type: 'discussion/thread',
                //         body: this.thread
                //     }, false)

                //     // Link the thead to the root folder.
                //     .then(({ id, type }) => {
                //         let linkage = { id, type }
                //         if (this.root)
                //             return tozti.store
                //                 .rels.add(this.root.body.children, {
                //                     [this.thread.handle]: linkage
                //                 })

                //         else {
                //             return tozti.api
                //                 .post(tozti.api.handleURL(this.thread.handle), {
                //                     data: linkage
                //                 })
                //         }
                //     })

                // handler(prom)
            }
        }
    }
</script>
