# -*- coding: utf-8 -*-

from faker.providers import BaseProvider

# Based loosely on https://tvtropes.org/pmwiki/pmwiki.php/Main/TechnoBabble
class SciFi(BaseProvider):
    technobabble = (
        ('reverse',
         'increase',
         'absorb',
         'melt',
         'release',
         'short circuit',
         'calculate',
         'use',
         'bypass',
         'inject',
         'blow',
         'instantiate',
         'generate',
         'induce',
         'accelerate',
         'close',
         'modify',
         'diable',
         'heat',
         'enhance',
         'disengage',
         'run'),
        ('the polarity of the',
         'the spacial',
         'the epithelial',
         'the warp',
         'the miniaturization',
         'the molecular',
         'the time-space',
         'the dimorphic',
         'the life-sustaining',
         'the submolecular',
         'the quark',
         'the pulse',
         'the flux',
         'the reality',
         'the dilithium',
         'the crystalline',
         'the distortion',
         'the quantum',
         'the heavy-ion',
         'a narrow beam of gravitonic',
         'the external inertial'),
        ('neutron flow',
         'linkage',
         'tissue',
         'core',
         'ray',
         'overloader',
         'coordinates',
         'system',
         'control',
         'grid',
         'parsecs',
         'inertia',
         'readings',
         'vortex',
         'energy',
         'wave',
         'emitters',
         'field',
         'radiation',
         'fusion',
         'dampener',
         'mainframe'))

    def babble(self):
        """
        :example 'reverse the polarity of the neutron flow'
        """
        result = []
        for phrase in self.technobabble:
            result.append(self.random_element(phrase))

        return " ".join(result)
