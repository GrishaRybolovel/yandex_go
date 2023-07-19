from api.models import Price

def main():
    Price.objects.create(price=191, point_from_x=49.1415029447, point_from_y=55.7854147855,
                         point_to_x=49.1546060789, point_to_y=55.8244056583)
    Price.objects.create(price=290, point_from_x=49.1415029447, point_from_y=55.7854147855,
                         point_to_x=49.1546060789, point_to_y=55.8244056583)
    Price.objects.create(price=319, point_from_x=49.1415029447, point_from_y=55.7854147855,
                         point_to_x=49.1546060789, point_to_y=55.8244056583)

if __name__ == '__main__':
    main()