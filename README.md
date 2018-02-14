# tozti-media
*An interface for viewing and managing your files in tozti.*

## Usage.

Once the dependencies are installed, you can use the following `npm` scripts.

- `npm run build` will compile all the .js, .vue, .sass files and all the assets of your extension for development.
- `npm run watch` will do the same as `npm run build`, but will automatically re-trigger when one of the files changes.
- `npm run release` will compile all the files of your extension for production use. 
   In particular, this means that all the files will be minified, and that source maps will be deleted.
- `npm run package` will run `npm run release`, and then package all of the compiled files into a .tar.gz archive.
