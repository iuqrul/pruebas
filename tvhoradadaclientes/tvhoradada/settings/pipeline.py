

PIPELINE_CSS = {
    'main': {
        'source_filenames': (
            'css/main.css',
        ),
        'output_filename': 'css/all.min.css',
    },
}




PIPELINE_JS = {
    'main': {
        'source_filenames': (

            'bower_components/jquery/jquery.js',
            'bower_components/lodash/dist/lodash.js',
            'bower_components/bootstrap/dist/js/bootstrap.js',
            'bower_components/angular-1.2.13/angular.js',
            'bower_components/angular-1.2.13/angular-animate.js',
            'bower_components/angular-1.2.13/i18n/angular-locale_es-es.js',
            'bower_components/angular-ui-router.min.js',
            'bower_components/restangular/src/restangular.js',
            'bower_components/angular-flash/dist/angular-flash.js',
            'bower_components/ui-bootstrap-custom-tpls-0.10.0.min.js',
            'js/utils.js',
            'js/app.js',
            'js/services.js',
            'js/controllers/*.js',

        ),
        'output_filename': 'all.min.js'
    }
}


STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'
STATICFILES_FINDERS = (
    'pipeline.finders.FileSystemFinder',
    'pipeline.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
    'pipeline.finders.CachedFileFinder'
)


PIPELINE_DISABLE_WRAPPER = True
PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.uglifyjs.UglifyJSCompressor'
