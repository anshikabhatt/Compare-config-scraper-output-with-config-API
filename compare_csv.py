import pandas as pd

scraper_output_df = pd.read_csv('scraper_output.csv')
file1_df = pd.read_csv('anshika.csv')
file2_df = pd.read_csv('abhishek_bhardwaj.csv')
file3_df = pd.read_csv('ahn_nath.csv')
file4_df = pd.read_csv('jaisakansha.csv')
file5_df = pd.read_csv('emile_daisy.csv')
file6_df = pd.read_csv('leilakaltouma.csv')

merged_file1_df = pd.merge(file1_df, scraper_output_df, on=['source language', 'target language'])
merged_file2_df = pd.merge(file2_df, scraper_output_df, on=['source language', 'target language'])
merged_file3_df = pd.merge(file3_df, scraper_output_df, on=['source language', 'target language'])
merged_file4_df = pd.merge(file4_df, scraper_output_df, on=['source language', 'target language'])
merged_file5_df = pd.merge(file5_df, scraper_output_df, on=['source language', 'target language'])
merged_file6_df = pd.merge(file6_df, scraper_output_df, on=['source language', 'target language'])

accuracy_file1_df = merged_file1_df[merged_file1_df['translation engine'] == merged_file1_df['engine name']]
accuracy_file1 = len(accuracy_file1_df) / len(scraper_output_df) * 100
print(f"Accuracy for anshika.csv: {accuracy_file1:.2f}%")

accuracy_file2_df = merged_file2_df[merged_file2_df['translation engine'] == merged_file2_df['engine name']]
accuracy_file2 = len(accuracy_file2_df) / len(scraper_output_df) * 100
print(f"Accuracy for abhishek_bhardwaj.csv: {accuracy_file2:.2f}%")

accuracy_file3_df = merged_file3_df[merged_file3_df['translation engine'] == merged_file3_df['engine name']]
accuracy_file3 = len(accuracy_file3_df) / len(scraper_output_df) * 100
print(f"Accuracy for ahn_nath.csv: {accuracy_file3:.2f}%")

accuracy_file4_df = merged_file4_df[merged_file4_df['translation engine'] == merged_file4_df['engine name']]
accuracy_file4 = len(accuracy_file4_df) / len(scraper_output_df) * 100
print(f"Accuracy for jaisakansha.csv: {accuracy_file4:.2f}%")

accuracy_file5_df = merged_file5_df[merged_file5_df['translation engine'] == merged_file5_df['engine name']]
accuracy_file5 = len(accuracy_file5_df) / len(scraper_output_df) * 100
print(f"Accuracy for emile_daisy.csv: {accuracy_file5:.2f}%")

accuracy_file6_df = merged_file6_df[merged_file6_df['translation engine'] == merged_file6_df['engine name']]
accuracy_file6 = len(accuracy_file6_df) / len(scraper_output_df) * 100
print(f"Accuracy for leilakaltouma.csv: {accuracy_file6:.2f}%")
