def gc_content(seq):
    """GC content of a given sequence"""
    seq = seq.upper()
    return (seq.count('G') + seq.count('C')) / len(seq)


def gc_blocks(seq, block_size):
    """
    Divide sequence into non-overlapping blocks
    and compute GC content of each block.
    """
    gc_blocks = []
    end = len(seq) - (len(seq) % block_size)
    for i in range(0, end, block_size):
        gc_blocks.append(gc_content(seq[i:i+block_size]))
    return gc_blocks

def gc_map(seq, block_size, gc_thresh):
    """Give back seq with lowercase letters where GC content is low."""

    out_seq = ''

    # Determine GC content of each block and change string accordingly
    for i in range(0, len(seq) - (len(seq) % block_size), block_size):
        if gc_content(seq[i:i+block_size]) < gc_thresh:
            out_seq += seq[i:i+block_size].lower()
        else:
            out_seq += seq[i:i+block_size].upper()

    return out_seq
