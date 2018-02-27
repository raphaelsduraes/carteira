from django.db import models
# Create your models here.
from django.db import models
import datetime



class Investimento(models.Model):
    tipo = models.CharField(max_length=20)
    taxa = models.FloatField(null=True, blank=True, default=None)
    instituicao_finaceira = models.CharField(max_length=30)
    valor_investido = models.FloatField(null=True, blank=True, default=None)
    corretora = models.CharField(max_length=20)
    data = models.DateField(blank=False)
    vencimento = models.DateField(blank=False)
    valor_atual = models.FloatField(null=True, blank=True, default=None)
    valor_liquido = models.FloatField(null=True, blank=True, default=None)
    imposto = models.FloatField(null=True, blank=True, default=None)
    projecao = models.FloatField(null=True, blank=True, default=None)

    def CalcDifDias(data1,data2):
        #d2 = datetime.strptime('2017-05-05', '%Y-%m-%d')
        #d1 = datetime.strptime('2017-05-01', '%Y-%m-%d')   
        difDias = abs((d2-d1).days)
        return difDias

    def CalculaImposto(data1,data2,tipo):
        difDias = 0
        taxaImp = 0
        if(tipo != "LCI" and tipo != "LCA"): 
            if(dif < 180):
                taxaImp = 0.225
            elif (dif >180 and dif < 360):
                taxaImp = 0.20;
            elif (dif >360 and dif < 720):
                taxaImp = 0.175;
            elif (dif >720):
                taxaImp = 0.15; 
        
        return taxaImp

class InvestimentoFixa(Investimento):



    def AtualizaInvestimento():
        valaux = self.valor_atual
        taxdiaria = (1+self.taxa)**(1/252) 
        valor_atual = valaux*taxdiaria