## Error analysis

### Slovene

```
paste <(grep -v '^#' ../datasets/sl/ssj500k/test.conllu|cut -f 5) <(cut -f 5 Parser-v3/ssj500k.test.conllu)|awk '{if ($1!=$2) print $0}'|sort|uniq -c|sort -rn > Parser-v3/ssj500k.test.conllu.conf
paste <(grep -v '^#' ../datasets/sl/ssj500k/test.conllu|cut -f 5) <(cut -f 5 reldi-tagger/ssj500k.test.conllu)|awk '{if ($1!=$2) print $0}'|sort|uniq -c|sort -rn > reldi-tagger/ssj500k.test.conllu.conf
paste reldi-tagger/ssj500k.test.conllu.conf Parser-v3/ssj500k.test.conllu.conf | head -n 20
    109 Ncmsan	Ncmsn	     58 Ncmsn	Npmsn
     71 Ncmsn	Ncmsan	     42 Ncmsan	Ncmsn
     61 Ncnsa	Ncnsn	     37 Ncmsn	Ncmsan
     47 Ncfpa	Ncfsg	     30 Pp3fpa--y	Pp3mpa--y
     41 Agpnsn	Rgp	     27 Cc	Rgp
     36 Ncfpn	Ncfsg	     19 Sa	Sl
     35 Ncnsn	Ncnsa	     17 Xf	Npmsn
     31 Agpnsa	Agpnsn	     17 Rgp	Agpnsn
     27 Sa	Sl	     17 Pp3nsa--y	Pp3msa--y
     27 Npmsay	Npmsg	     16 Ncnsn	Ncnsa
     27 Ncfpn	Ncfpa	     16 Agpnsn	Rgp
     25 Rgp	Agpnsn	     15 Vmem2p	Vmer2p
     25 Ncfpa	Ncfpn	     14 Ncnsa	Ncnsn
     25 Agpmsny	Agpmsay	     14 Ncfpn	Ncfsg
     25 Agpmsay	Agpmsny	     14 Agpmsny	Agpmsay
     23 Rgp	Cc	     12 Npmsn	Ncmsn
     23 Agpfpn	Agpfsg	     12 Ncfsn	Npfsn
     21 Pp3fpa--y	Pp3mpa--y	     11 Ncfpn	Ncfpa
     21 Npmsn	Npfsn	     10 Pp3npa--y	Pp3mpa--y
     21 Ncmsn	Npmsn	     10 Npmsan	Npmsn
```

### Croatian

```
paste <(grep -v '^#' ../datasets/hr/hr500k/test.conllu|cut -f 5) <(cut -f 5 Parser-v3/hr500k.test.conllu)|awk '{if ($1!=$2) print $0}'|sort|uniq -c|sort -rn > Parser-v3/hr500k.test.conllu.conf
paste <(grep -v '^#' ../datasets/hr/hr500k/test.conllu|cut -f 5) <(cut -f 5 reldi-tagger/hr500k.test.conllu)|awk '{if ($1!=$2) print $0}'|sort|uniq -c|sort -rn > reldi-tagger/hr500k.test.conllu.conf
paste reldi-tagger/hr500k.test.conllu.conf Parser-v3/hr500k.test.conllu.conf | head -n 20
    162 Xf	Npmsn	    128 Xf	Npmsn
    118 Qo	Cc	     68 Qo	Cc
    117 Ncmsan	Ncmsn	     57 Ncmsan	Ncmsn
     98 Ncmsn	Ncmsan	     56 Ncmsn	Ncmsan
     56 Ncfpa	Ncfsg	     52 Cs	Rgp
     55 Cs	Rgp	     51 Npmsn	Xf
     53 Ncmpg	Ncmsg	     49 Cc	Qo
     50 Ncmsg	Ncmpg	     48 Ncmsg	Ncmpg
     48 Agpnsny	Rgp	     44 Rgp	Cs
     43 Ncnsa	Ncnsn	     34 Ncmpg	Ncmsg
     42 Rgp	Cs	     29 Rgp	Agpnsny
     39 Cc	Qo	     27 Sa	Sl
     38 Ncnsn	Ncnsa	     25 Ncnsa	Ncnsn
     36 Npfsn	Npmsn	     23 Ncfpa	Ncfsg
     35 Sl	Sa	     22 Sl	Sa
     35 Npmsn	Xf	     21 Ncfpa	Ncfpn
     32 Sa	Sl	     20 Xf	Ncmsn
     32 Agpmsayn	Agpmsny	     19 Ncmsn	Npmsn
     28 Ncfpn	Ncfpa	     19 Ncfsn	Npfsn
     28 Agpmsny	Agpmsayn	     18 Npmsan	Npmsn
```

### Serbian

```
paste <(grep -v '^#' ../datasets/sr/SETimes.SR/test.conllu|cut -f 5) <(cut -f 5 Parser-v3/SETimes.SR.test.conllu)|awk '{if ($1!=$2) print $0}'|sort|uniq -c|sort -rn > Parser-v3/SETimes.SR.test.conllu.conf
paste <(grep -v '^#' ../datasets/sr/SETimes.SR/test.conllu|cut -f 5) <(cut -f 5 reldi-tagger/SETimes.SR.test.conllu)|awk '{if ($1!=$2) print $0}'|sort|uniq -c|sort -rn > reldi-tagger/SETimes.SR.test.conllu.conf
paste reldi-tagger/SETimes.SR.test.conllu.conf Parser-v3/SETimes.SR.test.conllu.conf | head -n 20
     28 Xf	Npmsn	     27 Xf	Npmsn
     22 Ncmsan	Ncmsn	      9 Npfsn	Npmsn
     13 Npmsan	Npmsn	      8 Npmsan	Npmsn
     12 Ncmsn	Ncmsan	      7 Ncmsn	Ncmsan
     12 Ncmsg	Ncmpg	      6 Ncnsn	Ncnsa
     12 Ncfpn	Ncfsg	      6 Ncmsg	Ncmpg
     11 Ncmpg	Ncmsg	      6 Ncmpg	Ncmsg
      9 Npmsay	Npmsg	      5 Npmsn	Npmsan
      8 Ncnsn	Ncnsa	      4 Ncmsan	Ncmsn
      8 Ncfpa	Ncfsg	      3 Var3s	Var3p
      8 Agpnsny	Rgp	      3 Sl	Sa
      7 Npfsn	Npmsn	      3 Sa	Sl
      6 Ncmsay	Ncmsg	      3 Npmsan	Xf
      6 Ncfsn	Ncfpg	      3 Npfsn	Npmsg
      5 Sa	Sl	      3 Ncmsg	Ncfsg
      5 Ncnsa	Ncnsn	      3 Ncmsd	Ncmsl
      5 Ncfsg	Ncfpa	      3 Ncfsn	Ncfpg
      4 Sl	Sa	      3 Agpmsny	Agpmsayn
      4 Ncfpi	Ncfpd	      3 Agpmpgy	Agpfpgy
      4 Agpmsdy	Agpmsly	      3 Agpfsny	Appfsny
```
