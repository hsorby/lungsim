
# Install the files needed to support installation via GNUmakefile.

# We need to generate the following
# include/configuration.mk:
# 	@echo "# include/configuration.mk generated automatically during build" \
# 		> include/configuration.mk
# 	@echo COMPILER  ?= $(COMPILER) >> include/configuration.mk
# 	@echo USEOPENMP ?= $(USEOPENMP) >> include/configuration.mk
# 	@echo USEMPI    ?= $(USEMPI) >> include/configuration.mk
# 	@echo BUILDROBUST ?= $(BUILDROBUST) >> include/configuration.mk
#   @echo VERSION ?= `cat VERSION` >> include/configuration.mk

function(file_compile_configuration)
   file(STRINGS "${CMAKE_CURRENT_SOURCE_DIR}/../VERSION" BUILD_VERSION)
   file(WRITE  ${CMAKE_CURRENT_BINARY_DIR}/include/configuration.mk "# include/configuration.mk generated automatically during build\n")
   file(APPEND ${CMAKE_CURRENT_BINARY_DIR}/include/configuration.mk "COMPILER  ?= ${CMAKE_Fortran_COMPILER_ID}\n")
   file(APPEND ${CMAKE_CURRENT_BINARY_DIR}/include/configuration.mk "USEOPENMP ?= ${OPENMP}\n")
   file(APPEND ${CMAKE_CURRENT_BINARY_DIR}/include/configuration.mk "USEMPI    ?= ${MPI}\n")
   if (PFUNIT_ROBUST)
      file(APPEND ${CMAKE_CURRENT_BINARY_DIR}/include/configuration.mk "BUILDROBUST ?= YES\n")
   else()
      file(APPEND ${CMAKE_CURRENT_BINARY_DIR}/include/configuration.mk "BUILDROBUST ?= \n")
   endif()
   file(APPEND ${CMAKE_CURRENT_BINARY_DIR}/include/configuration.mk "VERSION = \"${BUILD_VERSION}\"\n")
endfunction()

# message("***--- COMPILER:   ${COMPILER}")
# message("***--- BUILDROBUST:${PFUNIT_ROBUST}")

file_compile_configuration()

# add_custom_command(
#    OUTPUT configuration.mk
#    COMMAND file_compile_configuration
# )
# add_custom_target(configuration.mk ALL)

# Perform the install.
#
#install(FILES GNU.mk IBM.mk INTEL.mk NAG.mk PGI.mk extensions.mk driver.F90 DESTINATION include)
#install(FILES base-install.mk DESTINATION include RENAME base.mk)
#install(FILES ${CMAKE_CURRENT_BINARY_DIR}/include/configuration.mk DESTINATION include)
#install(FILES ${CMAKE_CURRENT_SOURCE_DIR}/TestUtil.F90 DESTINATION include)

