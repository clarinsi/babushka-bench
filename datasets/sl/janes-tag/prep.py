import random

random.seed(42)

train = []
dev = []
test = []
train_normed = []
dev_normed = []
test_normed = []
train_all = []
dev_all = []
test_all = []

with open('Janes-Tag.conllu/Janes-Tag.conllu', 'r', encoding='utf-8') as f:
    current_form = ''
    current_items = []
    current_lemma = []
    current_upos = []
    current_xpos = []
    current_feats = []
    current_misc = []
    for line in f:
        if line.startswith('# sent_id'):
            rand = random.random()
            if rand < 0.8:
                pointer = train
                pointer_normed = train_normed
                pointer_all = train_all
            elif rand < 0.9:
                pointer = dev
                pointer_normed = dev_normed
                pointer_all = dev_all
            else:
                pointer = test
                pointer_normed = test_normed
                pointer_all = test_all
            token_counter = 0
            norm_line = line
            all_line = line

        elif line.startswith('# text'):
            norm_line = line
            all_line = line

        elif line and line != '\n':
            idx, form, lemma, upos, xpos, feats, head, deprel, deps, misc = line.strip().split('\t')
            if '-' in idx:
                token_counter += 1
                current_items = [int(num) for num in idx.split('-')]
                current_form = form
                line = 'None'
            elif int(idx) in current_items:
                current_lemma.append(lemma)
                current_upos.append(upos)
                current_xpos.append(xpos)
                current_feats.append(feats)
                current_misc.append(misc)

                if int(idx) == current_items[-1]:
                    lemma = ' '.join(current_lemma)
                    upos = ' '.join(current_upos)
                    xpos = ' '.join(current_xpos)
                    feats = ' '.join(current_feats)
                    misc = ' '.join(current_misc)

                    current_items = []
                    current_lemma = []
                    current_upos = []
                    current_xpos = []
                    current_feats = []
                    current_misc = []

                    line = '\t'.join(
                        [str(token_counter), current_form, lemma, upos, xpos, feats, head, deprel, deps, misc, '\n'])

                else:
                    line = 'None'
            else:
                token_counter += 1
                line = '\t'.join([str(token_counter), form, lemma, upos, xpos, feats, head, deprel, deps, misc, '\n'])

            if line != 'None' and 'Normalized' in misc:
                misc_els = misc.split('|')
                norm = misc_els[0].split('=')[1]
                if len(misc_els) > 1:
                    misc = misc_els[1]
                else:
                    misc = '_'
                norm_line = '\t'.join([str(token_counter), norm, lemma, upos, xpos, feats, head, deprel, deps, misc, '\n'])
                all_line = '\t'.join([str(token_counter), form, norm, lemma, upos, xpos, feats, '\n'])
            else:
                norm_line = line
                all_line = '\t'.join([str(token_counter), form, form, lemma, upos, xpos, feats, '\n'])

        if line != 'None':
            pointer.append(line)
            pointer_normed.append(norm_line)
            pointer_all.append(all_line)


def write_list(lst, fname, all=False):
    with open(fname, 'w', encoding='utf-8') as f:
        if all:
            f.write('# global.columns = ID TOKEN NORM LEMMA UPOS XPOS FEATS\n')
        for el in lst:
            f.write(el)


write_list(train, 'train.conllu')
write_list(dev, 'dev.conllu')
write_list(test, 'test.conllu')
write_list(train_normed, 'train_normed.conllu')
write_list(dev_normed, 'dev_normed.conllu')
write_list(test_normed, 'test_normed.conllu')
write_list(train_all, 'train_all.conllup', all=True)
write_list(dev_all, 'dev_all.conllup', all=True)
write_list(test_all, 'test_all.conllup', all=True)
