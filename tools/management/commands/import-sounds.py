from os import listdir
from os.path import join, isfile, isdir, basename, dirname

from django.core.management.base import BaseCommand
from django.core.files import File

from tools.apps import REPLACEABLE_EQUIVALENCE, REPLACEABLE_ICONS_PATH
from tools.utils import cmd
from units.models import Race, Unit
from sounds.models import Sound


class Command(BaseCommand):
    help = """Import units sounds from a standard warcraft 3 mpq file tree"""

    def add_arguments(self, parser):
        parser.add_argument('-r', '--root', default='.',
                            help='Extracted mpq documents root')

    def handle(self, *args, **options):
        units_root = join(options['root'], 'Units')

        for race in listdir(units_root):
            race_root = join(units_root, race)
            if not isdir(race_root):
                continue

            self.handle_race(race)

            for unit in listdir(race_root):
                unit_root = join(race_root, unit)
                if not isdir(unit_root):
                    continue

                buttons = join(options['root'],
                               'ReplaceableTextures/CommandButtons')
                icon_path = join(buttons, 'BTN{}.blp'.format(unit))
                if not isfile(icon_path):
                    equivalence = REPLACEABLE_EQUIVALENCE.get(unit, None)
                    if equivalence is None:
                        self.stdout.write(
                            "{} not found for unit {} and its replaceable "
                            "icon is not defined".format(icon_path, unit))
                        continue

                    replaceable_icon = join(REPLACEABLE_ICONS_PATH,
                                            'BTN{}.blp'.format(equivalence))

                    icon_path = join(options['root'], replaceable_icon)
                    if not isfile(icon_path):
                        self.stdout.write(
                            "Unit {} has no icon and its replaceable icon {} "
                            "is not a file : using a question mark instead".
                            format(unit, icon_path))

                        question_mark = 'SelectHeroOn'
                        icon_path = join(options['root'],
                                         REPLACEABLE_ICONS_PATH,
                                         'BTN{}.blp'.format(question_mark))

                self.handle_unit(race, unit, icon_path)

                for sound in listdir(unit_root):
                    sound_path = join(unit_root, sound)
                    if not isfile(sound_path) or sound_path[-4:] != '.wav':
                        continue

                    self.handle_sound(race, unit, sound_path)

    def handle_race(self, race):
        r, created = Race.objects.get_or_create(
            name=race,
        )

    def beautiful_name(self, name):
        beautiful_name = name[0]
        for letter in name[1:]:
            if letter.isupper():
                beautiful_name += ' ' + letter.lower()
            else:
                beautiful_name += letter

        return beautiful_name

    def handle_unit(self, race, unit, icon):
        icon_dir = dirname(icon)
        cmd('BLPConverter', '--format', 'png', '--dest', icon_dir, icon)

        png_icon = icon[:-4] + '.png'

        r = Race.objects.get(name=race)
        with open(png_icon, 'rb') as fh:
            i = File(fh)
            Unit.objects.create(
                name=self.beautiful_name(unit),
                race=r,
                icon=i,
            )

    def handle_sound(self, race, unit, sound):
        r = Race.objects.get(name=race)
        u = Unit.objects.get(name=self.beautiful_name(unit), race=r)

        sound_name = basename(sound)[:-4]

        with open(sound, 'rb') as fh:
            s = File(fh)
            Sound.objects.create(
                name=sound_name,
                unit=u,
                audio=s,
            )