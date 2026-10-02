# W8D3: Haystack BM25 vs Dense Retrieval
# Same 5 PDFs and same 10 questions were used for both methods.
# Precision was calculated using top-3 retrieved documents.

bm25_precision = 0.40
dense_precision = 0.33

print("========== RETRIEVAL COMPARISON ==========")
print(f"BM25 Average Precision:   {bm25_precision:.2f}")
print(f"Dense Average Precision:  {dense_precision:.2f}")

difference = bm25_precision - dense_precision

print(f"Difference:               {difference:.2f}")

if difference > 0:
    print("BM25 performed better on this test set.")
elif difference < 0:
    print("Dense Retrieval performed better on this test set.")
else:
    print("Both methods produced the same precision.")

print("==========================================")
bm25_precision = 0.40
dense_precision = 0.33

print("========== RETRIEVAL COMPARISON ==========")
print(f"BM25 Average Precision:   {bm25_precision:.2f}")
print(f"Dense Average Precision:  {dense_precision:.2f}")

difference = bm25_precision - dense_precision

print(f"Difference:               {difference:.2f}")

if difference > 0:
    print("BM25 performed better on this test set.")
elif difference < 0:
    print("Dense Retrieval performed better on this test set.")
else:
    print("Both methods produced the same precision.")

print("==========================================")