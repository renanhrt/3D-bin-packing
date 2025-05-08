from py3dbp.main import Painter, Bin, Item, Packer

# init packing function
packer = Packer()

#  init bin
box = Bin(
    partno='small_pallet',         # partno / PN of item (unique value)
    WHD=(2200, 1600, 1100),       # (width , depth , height) 
    max_weight=2808000,     # box can bear the weight
    corner=0,             # container coner
    put_type= 1           # add the order of placing items
)

packer.addBin(box)

for i in range(4):
    item = Item(
        partno='G27600PR', # partno / PN of item (unique value)
        name='Tampo p/ balcao',       # type of item
        typeof='cube',     # cube or cylinder
        WHD=(610, 660, 36),  # (width , depth , height)
        weight=6.3,         # item weight
        level=2,           # priority (Item need to pack)
        loadbear=1000,      # item bearing, limit of wheight
        updown=False,       # item fall down or not
        color='#FFFF37'    # set item color
    )
    packer.addItem(item)

# calculate packing
packer.pack(
    bigger_first=True,                 # bigger item first.
    fix_point=True,                    # fix item float problem.
    binding=[('server','cabint')],     # make a set of items.
    distribute_items=True,             # If multiple bin, to distribute or not.
    check_stable=True,                 # check stability on item.
    support_surface_ratio=0.2,        # set support surface ratio.
    number_of_decimals=0
)

for b in packer.bins:
    b.new_center_items()
    for i, item in enumerate(b.items):
        pos = [float(p) for p in item.position]
        print(f"  ITEM {i}: {item.partno}")
        print(f"     Size      : {item.width} x {item.height} x {item.depth}")
        print(f"     Weight    : {item.weight}")
        print(f"     Position  : x={pos[0]}, y={pos[1]}, z={pos[2]}")
        print(f"     Rotation  : {item.rotation_type}")
        print(f"     Volume    : {item.getVolume()}")
        print("-" * 50)

    print(b.items)

    print("=" * 50)
    print(f"  BIN: {b.partno}")
    print(f"  Size: {b.width} x {b.height} x {b.depth}")
    print(f"  Max Weight: {b.max_weight}")
    print(f"  Volume: {b.getVolume()}")
    print(f"  Items Packed: {len(b.items)}")
    print("-" * 50)

    painter = Painter(b)
    fig = painter.plotBoxAndItems(
        title=b.partno,
        alpha=0.4, # transparancy of items
        write_num=True,
        fontsize=10
    )
fig.show()