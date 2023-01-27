include_directories(/home/lzc/z/cmake/t3/example/include
) #指定第三方头文件目录

link_directories()
# 指定第三方库文件目录

# 一定要先添加可执行文件再对其进行链接，顺序不能反掉了
add_executable(main main.c)
target_link_libraries(main /home/lzc/z/cmake/t3/example/lib/libhello.so)

# # 或者写成

# include_directories(/home/lzc/z/cmake/t3/example/include
# ) #指定第三方头文件目录

# link_directories(/home/lzc/z/cmake/t3/example/lib)
# # 指定第三方库文件目录

# # 一定要先添加可执行文件再对其进行链接，顺序不能反掉了
# add_executable(main main.c)
# target_link_libraries(main libhello.so)
