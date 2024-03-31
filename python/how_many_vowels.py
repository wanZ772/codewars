data = "The sun dipped below the horizon, painting the sky in hues of orange and pink. A gentle breeze rustled the leaves of the trees, carrying with it the scent of fresh grass. In the distance, a lone bird soared through the air, its silhouette stark against the fading light. As the day drew to a close, the world seemed to exhale, settling into a peaceful stillness that wrapped around everything like a warm blanket"
def count(the_string):
    vowels_count = 0
    vowels = {
        'a':0,
        'e':0,
        'i':0,
        'o':0,
        'u':0
    }
    for i in the_string.lower():
        if i in vowels:
            vowels[i] += 1
            vowels_count += 1
    return vowels, vowels_count
print(count(data))