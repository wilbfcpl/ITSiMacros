OLD_PREFIX='J FIC'
NEW_PREFIX='J PL FIC'
SAVED_PREFIX='J PL BOOK MYS'
AUTHOR_START_SAVED=14
AUTHOR_START_092=6
if OLD_PREFIX in record['092']['a']:
        author=record['590']['a'][AUTHOR_START_SAVED:]
        record['092']['a']=NEW_PREFIX + ' ' + author
