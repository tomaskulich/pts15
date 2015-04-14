var gulp = require('gulp');
var shell = require('gulp-shell')
var es6transpiler = require('gulp-es6-transpiler');
var out = require('gulp-out');
 
gulp.task('exec', ['transpile'], shell.task("node out.js"))

gulp.task('transpile', function () {
    return gulp.src('app.js')
        .pipe(es6transpiler())
        .pipe(out('out.js'));
});
