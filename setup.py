from distutils.core import setup

# Dynamically calculate the version based on tagging.VERSION.
version_tuple = __import__('voting').VERSION
if version_tuple[2] is not None:
    version = "%d.%d_%s" % version_tuple
else:
    version = "%d.%d" % version_tuple[:2]

setup(
    name='djangocms-applicants',
    version=version,
    description='Django CMS app for applications to events',
    author='Maik Berchten',
    author_email='mberchten@gmail.com',
    maintainer='Maik Berchten',
    maintainer_email='mberchten@gmail.com',
    url='https://github.com/ForumDev/djangocms-applicants',
    packages=[
        'applicants',
        'applicants.migrations',
        'applicants.templatetags',
        'applicants.tests',
    ],
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django CMS',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ],
)
