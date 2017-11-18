import maydate

pairs = [(13, 11.9),  # TTTT
         (13, 12), (13, 12.1), (13, 13.9), (13, 14),  # TTFF
         (13, 14.1), (13, 16), (14, 12.9),  # TTTT
         (14, 13), (14, 13.1), (14, 14.9), (14, 15),  # TTFF
         (14, 15.1), (14, 16), (15, 13.9),  # TTT
         (15, 14), (15, 14.1),  # TTFF
         (15, 14.5), (15, 15.9), (15, 16),  # FFFF
         (15, 16.1), (16, 14.9),  # TT
         (16, 15.1), (16, 16.9), (16, 17), (16, 17.1), (23.4, 24.3)  # FFFFF
         ]
for pair in pairs:
    first = pair[0]
    second = pair[1]
    print(maydate.creepy(first, second), maydate.creepy(second, first),
          maydate.creepy_permissive(first, second),
          maydate.creepy_permissive(second, first))
