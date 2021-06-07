import pandas as pd

def create_celebahq_train_val_txt_file(train_txt_path, val_txt_path):
    df = pd.read_csv('image_list.txt', delim_whitespace=True)
    df['idx'] = [str(idx).zfill(5) for idx in df['idx']]
    df['orig_idx'] = [str(orig_idx + 1).zfill(6) for orig_idx in df['orig_idx']]
        
    net2net_name_to_original_name = {idx: orig_idx for idx, orig_idx in zip(df['idx'], df['orig_idx'])}
    
    with open(train_txt_path) as t:
        train_net2net_file_names = t.read().splitlines()
    new_train_filenames = [net2net_name_to_original_name[str(train_file_name[5:10])] + '.jpg' for train_file_name in train_net2net_file_names]
        
    with open(val_txt_path) as v:
        val_net2net_file_names = v.read().splitlines()
    new_val_filenames = [net2net_name_to_original_name[str(val_file_name[5:10])] + '.jpg' for val_file_name in val_net2net_file_names]
        
    with open('new_celebahqtrain.txt', 'w') as t:
        t.writelines("\n".join(new_train_filenames))
        
    with open('new_celebahqvalidation.txt', 'w') as v:
        v.writelines("\n".join(new_val_filenames))
    
if __name__ == '__main__':
    train_txt_path, val_txt_path = 'celebahqtrain.txt', 'celebahqvalidation.txt' # can be found in /net2net/data
    create_celebahq_train_val_txt_file(train_txt_path, val_txt_path)