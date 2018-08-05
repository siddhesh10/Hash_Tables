import sys
sys.path.insert(0,"C:/Users/sidd/Desktop/Hash_Tables/")
import hash_tables

my_hash_table=hash_tables.hash_tables()
my_hash_table.add_to_table("s",12)
my_hash_table.add_to_table("q",13)
my_hash_table.add_to_table("w",15)
my_hash_table.add_to_table("v",17)
my_hash_table.add_to_table("b",19)
my_hash_table.show()
my_hash_table.remove("w")
my_hash_table.show()
