## Error analysis

### Slovene

Parser-v3

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

stanfordnlp 

```
paste <(grep -v '^#' ../datasets/sl/ssj500k/test.conllu|cut -f 5) <(cut -f 5 stanfordnlp/ssj500k.test.emb_conll.conllu)|awk '{if ($1!=$2) print $0}'|sort|uniq -c|sort -rn > stanfordnlp/ssj500k.test.emb_conll.conllu.conf
paste <(grep -v '^#' ../datasets/sl/ssj500k/test.conllu|cut -f 5) <(cut -f 5 stanfordnlp/ssj500k.test.emb_clarinft.conllu)|awk '{if ($1!=$2) print $0}'|sort|uniq -c|sort -rn > stanfordnlp/ssj500k.test.emb_clarinft.conllu.conf
paste <(grep -v '^#' ../datasets/sl/ssj500k/test.conllu|cut -f 5) <(cut -f 5 reldi-tagger/ssj500k.test.conllu)|awk '{if ($1!=$2) print $0}'|sort|uniq -c|sort -rn > reldi-tagger/ssj500k.test.conllu.conf
paste reldi-tagger/ssj500k.test.conllu.conf stanfordnlp/ssj500k.test.emb_conll.conllu.conf stanfordnlp/ssj500k.test.emb_clarinft.conllu.conf | head -n 20

    109 Ncmsan	Ncmsn	     55 Ncmsn	Npmsn	     54 Ncmsn	Npmsn
     71 Ncmsn	Ncmsan	     31 Pp3fpa--y	Pp3mpa--y	     31 Pp3fpa--y	Pp3mpa--y
     61 Ncnsa	Ncnsn	     31 Ncmsn	Ncmsan	     28 Ncmsan	Ncmsn
     47 Ncfpa	Ncfsg	     25 Ncmsan	Ncmsn	     28 Cc	Rgp
     41 Agpnsn	Rgp	     24 Cc	Rgp	     27 Ncmsn	Ncmsan
     36 Ncfpn	Ncfsg	     20 Rgp	Agpnsn	     20 Xf	Npmsn
     35 Ncnsn	Ncnsa	     18 Npfsn	Npmsn	     18 Ncnsn	Ncnsa
     31 Agpnsa	Agpnsn	     18 Agpnsn	Rgp	     17 Pp3nsa--y	Pp3msa--y
     27 Sa	Sl	     17 Xf	Npmsn	     17 Npfsn	Npmsn
     27 Npmsay	Npmsg	     17 Pp3nsa--y	Pp3msa--y	     17 Mlc-pn	Mlc-pa
     27 Ncfpn	Ncfpa	     16 Mlc-pn	Mlc-pa	     15 Rgp	Agpnsn
     25 Rgp	Agpnsn	     14 Ncnsn	Ncnsa	     15 Agpnsn	Rgp
     25 Ncfpa	Ncfpn	     14 Ncnsa	Ncnsn	     14 Sa	Sl
     25 Agpmsny	Agpmsay	     14 Ncfpn	Ncfsg	     13 Ncnsa	Ncnsn
     25 Agpmsay	Agpmsny	     13 Sa	Sl	     12 Ncfsn	Npfsn
     23 Rgp	Cc	     13 Ncfpa	Ncfpn	     11 Xf	Ncmsn
     23 Agpfpn	Agpfsg	     12 Vmem2p	Vmer2p	     11 Npmsn	Npfsn
     21 Pp3fpa--y	Pp3mpa--y	     12 Npmsn	Ncmsn	     11 Npmsn	Ncmsn
     21 Npmsn	Npfsn	     11 Npmsn	Npfsn	     11 Npmsay	Npmsg
     21 Ncmsn	Npmsn	     11 Ncmsn	Ncmsnn	     10 Vmem2p	Vmer2p

```

### Croatian

Parser-v3

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

stanfordnlp

```
paste <(grep -v '^#' ../datasets/hr/hr500k/test.conllu|cut -f 5) <(cut -f 5 stanfordnlp/hr500k.test.emb_conll.conllu)|awk '{if ($1!=$2) print $0}'|sort|uniq -c|sort -rn > stanfordnlp/hr500k.test.emb_conll.conllu.conf
paste <(grep -v '^#' ../datasets/hr/hr500k/test.conllu|cut -f 5) <(cut -f 5 stanfordnlp/hr500k.test.emb_clarinft.conllu)|awk '{if ($1!=$2) print $0}'|sort|uniq -c|sort -rn > stanfordnlp/hr500k.test.emb_clarinft.conllu.conf
paste <(grep -v '^#' ../datasets/hr/hr500k/test.conllu|cut -f 5) <(cut -f 5 reldi-tagger/hr500k.test.conllu)|awk '{if ($1!=$2) print $0}'|sort|uniq -c|sort -rn > reldi-tagger/hr500k.test.conllu.conf
paste reldi-tagger/hr500k.test.conllu.conf stanfordnlp/hr500k.test.emb_conll.conllu.conf stanfordnlp/hr500k.test.emb_clarinft.conllu.conf | head -n 20

    162 Xf	Npmsn	    172 Xf	Npmsn	    111 Xf	Npmsn
    118 Qo	Cc	     94 Cs	Rgp	     96 Qo	Cc
    117 Ncmsan	Ncmsn	     91 Cc	Qo	     75 Cs	Rgp
     98 Ncmsn	Ncmsan	     60 Mro	Mdo	     74 Npmsn	Xf
     56 Ncfpa	Ncfsg	     56 Ncmsn	Ncmsan	     57 Mro	Mdo
     55 Cs	Rgp	     46 Ncmpg	Ncmsg	     50 Ncmsg	Ncmpg
     53 Ncmpg	Ncmsg	     45 Ncmsg	Ncmpg	     42 Ncmsan	Ncmsn
     50 Ncmsg	Ncmpg	     41 Qo	Cc	     38 Ncmpg	Ncmsg
     48 Agpnsny	Rgp	     40 Ncmsan	Ncmsn	     37 Rgp	Cs
     43 Ncnsa	Ncnsn	     34 Xf	Ncmsn	     36 Cc	Qo
     42 Rgp	Cs	     29 Npmsn	Xf	     32 Ncmsn	Ncmsan
     39 Cc	Qo	     27 Ncmsn	Npmsn	     30 Sa	Sl
     38 Ncnsn	Ncnsa	     26 Sa	Sl	     27 Ncnsa	Ncnsn
     36 Npfsn	Npmsn	     26 Agpnsny	Rgp	     26 Rgp	Agpnsny
     35 Sl	Sa	     24 Npmsn	Npfsn	     24 Xf	Ncmsn
     35 Npmsn	Xf	     24 Ncfsn	Npfsn	     23 Sl	Sa
     32 Sa	Sl	     23 Sl	Sa	     23 Ncfsn	Npfsn
     32 Agpmsayn	Agpmsny	     23 Rgp	Cs	     21 Agpnsny	Rgp
     28 Ncfpn	Ncfpa	     23 Npfsn	Npmsn	     20 Ncmsn	Npmsn
     28 Agpmsny	Agpmsayn	     22 Npmsan	Npmsn	     20 Ncfpa	Ncfsg
```


### Serbian

Parser-v3

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

stanfordnlp
```
paste <(grep -v '^#' ../datasets/sr/SETimes.SR/test.conllu|cut -f 5) <(cut -f 5 stanfordnlp/SETimes.SR.test.emb_clarinft.conllu)|awk '{if ($1!=$2) print $0}'|sort|uniq -c|sort -rn > stanfordnlp/SETimes.SR.test.emb_clarinft.conllu.conf
paste <(grep -v '^#' ../datasets/sr/SETimes.SR/test.conllu|cut -f 5) <(cut -f 5 reldi-tagger/SETimes.SR.test.conllu)|awk '{if ($1!=$2) print $0}'|sort|uniq -c|sort -rn > reldi-tagger/SETimes.SR.test.conllu.conf
paste reldi-tagger/SETimes.SR.test.conllu.conf stanfordnlp/SETimes.SR.test.emb_clarinft.conllu.conf | head -n 20
     28 Xf	Npmsn	     20 Xf	Npmsn
     22 Ncmsan	Ncmsn	     10 Ncmsan	Ncmsn
     13 Npmsan	Npmsn	     10 Ncmpg	Ncmsg
     12 Ncmsn	Ncmsan	      8 Npfsn	Npmsn
     12 Ncmsg	Ncmpg	      8 Ncmsn	Ncmsan
     12 Ncfpn	Ncfsg	      7 Npmsan	Npmsn
     11 Ncmpg	Ncmsg	      5 Ncnsn	Ncnsa
      9 Npmsay	Npmsg	      5 Ncmsg	Ncmpg
      8 Ncnsn	Ncnsa	      4 Npmsn	Npmsan
      8 Ncfpa	Ncfsg	      4 Ncnsa	Ncnsn
      8 Agpnsny	Rgp	      4 Agpfsny	Appfsny
      7 Npfsn	Npmsn	      3 Rgp	Agpnsny
      6 Ncmsay	Ncmsg	      3 Pi3n-a	Pi3n-n
      6 Ncfsn	Ncfpg	      3 Pd-mpn	Pp3mpn
      5 Sa	Sl	      3 Npnsn	Npmsn
      5 Ncnsa	Ncnsn	      3 Npmsay	Npmsn
      5 Ncfsg	Ncfpa	      3 Npmsan	Xf
      4 Sl	Sa	      3 Ncfpi	Ncfpd
      4 Ncfpi	Ncfpd	      3 Agpmpgy	Agpfpgy
      4 Agpmsdy	Agpmsly	      2 Xf	Cc
```
