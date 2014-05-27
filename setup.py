from distutils.core import setup
from distutils.extension import Extension

try:
    from Cython.Distutils import build_ext
except ImportError:
    use_cython = False
else:
    use_cython = True

cmdclass = { }
ext_modules = [ ]

if use_cython:
    ext_modules += [
        Extension("query_integral_image", [ 'wordcloud/query_integral_image.pyx' ]),
    ]
    cmdclass.update({ 'build_ext': build_ext })
else:
    ext_modules += [
        Extension("query_integral_image", [ 'wordcloud/query_integral_image.c' ]),
    ]

setup(
    name='wordcloud',
    version='1.0.0',
    url='https://github.com/niklasp/word_cloud',
    license='MIT',
    cmdclass= cmdclass,
    ext_modules=ext_modules,
    packages=['wordcloud'],
    package_data={'wordcloud': ['stopwords']}
)
