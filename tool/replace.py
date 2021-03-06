import sys
enc='iso-8859-15'
with open(sys.argv[1], 'r', encoding=enc) as f:
    content = f.read()
    replacements = [
        ('osg::Vec3f', 'glm::vec3'),
        ('osg::Vec4f', 'glm::vec4'),
        ('osgHimmel', 'glHimmel'),
        ('"declspec.h"', '<glhimmel-computed/glhimmel-computed_api.h>'),
        ('t_julianDay', 'JulianDay'),
        ('t_aTime', 'AstronomicalTime'),
        ('OSGH_API', 'GLHIMMEL_COMPUTED_API'),
        ('t_longf', 'long double'),
        ('osg::Matrixf::rotate', 'glm::rotate'),
        ('osg::Matrixf', 'glm::mat4'),
        ('asin(', 'asin###('),
        ('atan2(', 'atan2###('),
        ('acos(', 'acos###('),
        ('sin(', 'std::sin('),
        ('cos(', 'std::cos('),
        ('tan(', 'std::tan('),
        ('asin###(', 'std::asin('),
        ('atan2###(', 'std::atan2('),
        ('acos###(', 'std::acos('),
        ('_rad(', 'glm::radians('),
        ('_deg(', 'glm::degrees('),
        ('osg::Program *', 'globjects::ref_ptr<globjects::Program> '),
        ('<osg/Vec3f>', '<glm/vec3>'),
        ('assert.h', 'cassert'),
        ('math.h', 'cmath'),
        ('t_equd', 'EquatorialCoords<long double>'),
        ('t_hord', 'HorizontalCoords<long double>'),
        ('t_ecld', 'EclipticalCoords<long double>'),
        ('t_equd', 'EquatorialCoords<long double>'),
        ('t_hord', 'HorizontalCoords<long double>'),
        ('t_ecld', 'EclipticalCoords<long double>'),
        ('NULL', 'nullptr'),
        ('osg::Texture2D', 'globjects::Texture'),
        ('osg::Texture3D', 'globjects::Texture'),
    ]
    for k, v in replacements:
        content = content.replace(k, v)

    new_content = ""
    if sys.argv[1].endswith('.cpp'):
        include = False
        for n in content.splitlines():
            if n.startswith('#include'):
                include = True
            if include:
                new_content += n + '\n'
    elif sys.argv[1].endswith('.h'):
        pragma = False
        for n in content.splitlines():
            if n.startswith('#pragma'):
                pragma = True
            if (n.startswith('#ifndef __') or
                    n.startswith('#define __') or
                    n.startswith('#endif // __')):
                continue
            if pragma:
                new_content += n + '\n'
    content = new_content

    new_content = ""
    for n in content.splitlines():
        n = n.rstrip()
        if n.startswith('#include "'):
            n = n.replace('#include "', '#include <glhimmel-computed/')
            n = n.replace('"', '>')
        n.replace('\t', '    ')
        new_content += n + '\n'
    content = new_content


with open(sys.argv[1], 'w') as f:
    f.write(content)
