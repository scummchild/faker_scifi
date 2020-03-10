# faker_scifi
faker_scifi is a community provider for the Faker test data generator Python package.  This package creates science fiction technobabble text (e.g., "reverse the polarity of the neutron flow") just for a little nerdy fun.

Thanks, https://github.com/SkypLabs/faker-wifi-essid for providing a very nice template to follow!

Here's the link to the main Faker project: https://github.com/joke2k/faker

Here's where a lot of the technobabble came from:
   * https://tvtropes.org/pmwiki/pmwiki.php/Main/TechnoBabble
   * https://youtu.be/naXLxNX4UZc

Usage
-----
Install with setup.py:

```bash

    git clone https://github.com/scummchild/faker_scifi
    cd faker_scifi && python setup.py install
```
Add the ``SciFi`` provider to your ``Faker`` instance:

```python

    from faker import Faker
    from faker_scifi import SciFi

    fake = Faker()
    fake.add_provider(SciFi)

    for _ in range(1,5):
        fake.babble()

        # 'short circuit the heavy-ion core'
        # 'inject the time-space grid'
        # 'calculate a narrow beam of gravitonic coordinates'
        # 'accelerate the external inertial emitters'
```
