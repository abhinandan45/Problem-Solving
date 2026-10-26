lis = [2,3,2,5,6,7,8,9]

m_n = float("inf")
sec_min = float("inf")

for i in lis:
    if i < m_n:
        sec_min = m_n
        m_n = i

    if i < sec_min and i != m_n:
        sec_min = i

print(sec_min)