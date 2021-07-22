import os
import hashlib
# import sys

# walk_dir = sys.argv[1]    # to take path as argument

compromised = 'compromised'
original = 'original'
walk_dir = compromised

print("Walk dir = " + walk_dir)
print("Walk dir (absolute) = " + os.path.abspath(walk_dir))

for root, subdirs, files in os.walk(walk_dir):
    # print('..\nroot = ' + root)
    list_file_path = os.path.join(root, 'my-directory-list.txt')
    # print('list_file_path = ' + list_file_path)

    with open(list_file_path, 'wb') as list_file:
    #     # for subdir in subdirs:
    #     #     print('\t- subdirectory' + subdir)

        for filename in files:
            compromised_file_path = os.path.join(root, filename)
            original_file_path = compromised_file_path.replace(compromised, original)
            # print("\n" + compromised_file_path + "\t" + original_file_path + "\n")

            try:
                compromised_md5 = hashlib.md5(open(compromised_file_path, 'r').read().encode('utf-8'))
                original_md5 = hashlib.md5(open(original_file_path, 'r').read().encode('utf-8'))
                # print(original_md5.hexdigest())
                if(compromised_md5.hexdigest() != original_md5.hexdigest()):
                    print("(#) modified file is:\t%s" % compromised_file_path)
            except(Exception):
                print("(#) newly created file detected:\t%s" % compromised_file_path)

            # with open(compromised_file_path, 'rb') as f:
            #     f_content = f.read()
            #     list_file.write(('The file %s contains:\n' %filename).encode('utf-8'))
            #     list_file.write(f_content)
            #     list_file.write(b'\n')