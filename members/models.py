from django.db import models
from django.utils.translation import ugettext as _

class Member( models.Model ):
  mitglied_nr = models.AutoField( primary_key=True, verbose_name=_('Member #') )
  aktiv = models.BooleanField( default=True, verbose_name=_('Active?') )  
  nachname = models.CharField( max_length=200, verbose_name=_('Lastname') )
  vorname = models.CharField( max_length=200, verbose_name=_('Firstname') )
  plz = models.IntegerField( verbose_name=_('Postal Code') )
  stadt = models.CharField( max_length=50, verbose_name=_('City') )
  strasse = models.CharField( max_length=200, verbose_name=_('Address') )
  geburtstag = models.DateField( null=True, blank=True, verbose_name=_('Birthdate') )
  telefon = models.CharField( max_length=50, null=True, blank=True, verbose_name=_('Phone') )
  mobil = models.CharField( max_length=50, null=True, blank=True, verbose_name=_('Cellphone') )
  webseite = models.CharField( max_length=200, null=True, blank=True, verbose_name=_('Homepage') )
  email = models.EmailField( verbose_name=_('Email'))
  email2 = models.EmailField( null=True, blank=True, verbose_name=_('Email2') )
  cacert_assurer = models.BooleanField(verbose_name=_('CACert Assurer'))
  pgp_signer = models.BooleanField(verbose_name=_('GPG-Signer'))
  beitrag_ab = models.DateField(verbose_name=_('Fee from'))
  mitglied_seit = models.DateField(verbose_name=_('Member since'))
  lastschrift = models.BooleanField(verbose_name=_('ELV'))
  bank = models.CharField( max_length=100, null=True, blank=True, verbose_name=_('Bank') )
  blz = models.IntegerField( null=True, blank=True, verbose_name=_('Bank ID') )
  konto_nr = models.IntegerField( null=True, blank=True, verbose_name=_('Account') )
  konto_inh = models.CharField( max_length=100, null=True, blank=True, verbose_name=_('Account Owner') )
  iban = models.CharField( max_length=34, null=True, blank=True, verbose_name=_('IBAN') )
  bic = models.CharField( max_length=11, null=True, blank=True, verbose_name=_('BIC') )
  current_separef = models.CharField( max_length=16, null=True, blank=True, verbose_name=_('current SEPA reference') )
  sepa_autopay = models.BooleanField( verbose_name=_('SEPA Autopayments') )
  bemerkung = models.TextField( null=True, blank=True, verbose_name=_('Comment') )
  funktion = models.CharField(max_length=100, null=True, blank=True, verbose_name=_('Function') )
  
  class Meta:
    verbose_name = _('member')
    verbose_name_plural = _('members')

  def __unicode__(self):
    return self.fullname()
    
  def fullname(self):
    return self.vorname+' '+self.nachname
    
  fullname.short_description = _('Name')

