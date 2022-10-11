import math


def progress_bar(progress, total):
    """ 
    Fonction de calcul et d'affichage de progression sur 
    le terminal.
    """
    percent = 100 * (progress / float(total));
    bar     = 'O' * int(percent) + '-' * int(100 - float(percent));
    print(f"\r|{bar}| {percent:.2f}%", end='\r');
    if progress == total:
        # si la progression est complette, alors
        # on retourne a la ligne
        print();
        return 1;


if __name__ == '__main__':
    numbers = [x * 5 for x in range(2000, 3000)];
    results = [];

    progress_bar(0, len(numbers));
    for i, x in enumerate(numbers):
        results.append(math.factorial(x));
        progress_bar(i + 1, len(numbers));


