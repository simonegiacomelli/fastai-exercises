import tarfile

with tarfile.open("../data/tri_and_rect.tgz", "w:gz") as tar:
    tar.add("../data/tri_and_rect", arcname='tri_and_rect')
