#3. Buatlah fungsi untuk melihat keterangan lulus atau tidak lulus : 

def lulus_tidak(nilai):

    if nilai > 60:
        return 'Lulus'
    else:
        return 'Tidak Lulus'

nilai_kamu= 80
hasil= lulus_tidak(nilai_kamu)
print(f'A.) Nilai Kamu: {nilai_kamu}, Status Nilai: {hasil}')

nilai_kamu2= 60
hasil2= lulus_tidak(nilai_kamu2)
print(f'B.) Nilai Kamu: {nilai_kamu2}, Status Nilai: {hasil2}')