import os
import numpy as np

def load_filenames(folderpath):
    filenames = os.listdir(folderpath)
    filenames = [f for f in filenames if f.endswith('.jpg')]
    filenames.sort(key=lambda x: int(x.split('.')[0]))
    return filenames

def sort_interleaved_pages(filenames, start_index_interleaved):
    N = len(filenames)
    M = start_index_interleaved
    left_pages = filenames[:M]
    right_pages = filenames[M:][::-1]
    sorted_filenames = []
    for i in range(N):
        if i % 2 == 0:
            sorted_filenames.append(left_pages[i // 2])
        else:
            sorted_filenames.append(right_pages[i // 2])
    return sorted_filenames


if __name__ == "__main__":
    folderpath = '/Users/reingel/Downloads/Scanned_book/'
    filenames = load_filenames(folderpath)
    start_index_interleaved = int(np.ceil(len(filenames) / 2))
    sorted_filenames = sort_interleaved_pages(filenames, start_index_interleaved)
    new_filenames = [f'{idx}.jpg' for idx in range(100, 100 + len(filenames))]
    paired = zip(sorted_filenames, new_filenames)
    for old_name, new_name in paired:
        old_path = os.path.join(folderpath, old_name)
        new_path = os.path.join(folderpath, new_name)
        print(f'Renaming {old_name} to {new_name}')
        os.rename(old_path, new_path)
    print('All done.')
