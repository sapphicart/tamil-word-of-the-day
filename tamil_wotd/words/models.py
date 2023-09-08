from django.db import models
# import sys
import random
import os
from django.utils import timezone

# Create your models here.

CD = os.path.dirname(os.path.realpath(__file__))
TXTFILE = os.path.join(CD, 'tamil_words.txt')

def words():
    file = open(TXTFILE, 'r', encoding='utf-8') 
    search_list = file.read().split('\n')
    file.close()

    search_dict = {}
    for i in range(len(search_list)):
        search_dict[i] = search_list[i]

    # first_key, first_value = next(iter(search_dict.items()))
    # sys.stdout.buffer.write(f"{first_key}: {first_value}".encode('utf-8'))

    word = random.choice(list(search_dict.values()))

    """with open('output.txt', 'w', encoding='utf-8') as output_file:
        output_file.write(word)"""

    return word

class Words(models.Model):
    id = models.AutoField(primary_key=True)
    word = models.CharField(verbose_name="Word", max_length=100, unique=True)
    meaning = models.TextField(verbose_name="Meaning")
    transliteration = models.CharField(verbose_name="Transliteration", max_length=100)
    example = models.TextField(verbose_name="Example")
    date = models.DateField(verbose_name="Date", default=timezone.now)

    def random_word(self):
        return words()

    def save(self, *args, **kwargs):
        if not self.word:
            self.word = self.random_word()
        super(Words, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Words"

    def __str__(self):
        return '%s, %s, %s, %s' % (self.word, self.meaning, self.transliteration, self.example)
