import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8')
CORES = {
    "azul_principal": "#1F5C99",
    "verde_secundario": "#3A7D44",
    "fundo": "#FFFFFF",
    "texto": "#222222",
    "grid": "#E0E0E0"
}


enpeh = {'ANO': [1995, 1997, 1999, 2001, 2003, 2006, 2008, 2011, 2013, 2017, 2019],
         'ARTIGOS': [25, 90, 78, 103, 105, 94, 132, 206, 129, 86, 209]}

perspectivas = {'ANO': [1988, 1996, 1998, 2001, 2004, 2007, 2009, 2012, 2015, 2018, 2020],
                'ARTIGOS': [41, 42, 73, 51, 100, 233, 213, 261, 206, 144, 118]}


fig, ax = plt.subplots(figsize=(12, 5.5))

# Plot das linhas
ax.plot(enpeh['ANO'], enpeh['ARTIGOS'], 
        marker='o', linestyle='-', linewidth=2.3, 
        markersize=8, markeredgewidth=1.3,
        color=CORES["azul_principal"], 
        markeredgecolor='white',
        label='ENPEH')

ax.plot(perspectivas['ANO'], perspectivas['ARTIGOS'], 
        marker='s', linestyle='-', linewidth=2.3, 
        markersize=8, markeredgewidth=1.3,
        color=CORES["verde_secundario"], 
        markeredgecolor='white',
        label='PERSPECTIVAS')


ax.set_xlabel('Ano', fontsize=11, labelpad=8, color=CORES["texto"])
ax.set_ylabel('Número de Artigos', fontsize=11, labelpad=8, color=CORES["texto"])

all_years = sorted(list(set(enpeh['ANO'] + perspectivas['ANO'])))
ax.set_xticks(all_years)
ax.set_xticklabels(all_years, rotation=45, ha='right', fontsize=10)
ax.set_yticks(range(0, 301, 50))
ax.set_yticklabels(range(0, 301, 50), fontsize=10)
ax.set_xlim(1987, 2021)
ax.set_ylim(0, 300)

ax.grid(True, linestyle='--', linewidth=0.6, alpha=0.7, color=CORES["grid"])
ax.set_facecolor(CORES["fundo"])
fig.set_facecolor(CORES["fundo"])

legend = ax.legend(frameon=True, fontsize=10, 
                  facecolor='white', framealpha=1,
                  borderpad=0.8, handlelength=1.8,
                  edgecolor=CORES["grid"], loc='upper left')


plt.savefig('producao_academica_final.pdf', format='pdf', bbox_inches='tight')
plt.savefig('producao_academica_final.png', dpi=600, bbox_inches='tight')


plt.tight_layout()
plt.show()

print("Arquivos exportados com sucesso:")
print("- producao_academica_final.pdf")
print("- producao_academica_final.png")
